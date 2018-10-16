"""
部署前，请确保机器上有virtualenv
"""
import logging
import sys
import os
from configobj import ConfigObj

from fabric import Connection, task

os.environ["INVOKE_RUN_ECHO"] = "1"
logging.basicConfig(level=logging.INFO,
                    format='%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
config_dict = {
    "system_python": "/bin/python3",
    "work_dir": "/home/rongbo/autointerface",
    "package_file_name": "autointerface-0.0.1.tar.gz",
    "config_file_name": "config_dev.py",
    "host": "yi@123.56.75.209:62124"
}


def load_config(env):
    try:
        config = ConfigObj("fabric.ini", file_error=True, encoding='UTF-8')
    except IOError:
        logging.fatal("fabric.ini不存在，执行fab init命令将在当前路径下生成默认配置")
        sys.exit(-1)
    except SyntaxError as e:
        logging.fatal("fabric.ini文件存在错误: %s" % str(e))
        sys.exit(-1)
    else:
        if env not in config:
            logging.fatal("fabric.ini不存在名为%s的区块" % env)
            sys.exit(-1)
        for key in config_dict:
            if key not in config[env]:
                logging.fatal("fabric.ini中%s区块的%s字段不存在" % (env, key))
                sys.exit(-1)
            config_dict[key] = config[env][key]
    return config_dict


def upload(connection,
           local_path, local_file_name,
           remote_path, remote_file_name):
    local_full_name = os.path.join(local_path, local_file_name)
    result = connection.put(local_full_name, remote=remote_path)
    logging.info("【文件{local_file_name}上传】OK {0.local} => {0.remote}".format(
        result, local_file_name=local_file_name))

    if local_file_name != remote_file_name:
        config_rename_cmd = "mv {config_file_name} {remote_file_name}".format(
            config_file_name=local_file_name,
            remote_file_name=remote_file_name
        )
        with connection.cd(remote_path):
            connection.run(config_rename_cmd)
            logging.info(
                "【配置{remote_file_name}重命名】OK {config_file_name} => {remote_file_name}".format(
                    config_file_name=local_file_name,
                    remote_file_name=remote_file_name
                ))


def create_dir(connection, directory):
    test_work_dir_cmd = "test -f {directory}".format(
        directory=directory)
    if connection.run(test_work_dir_cmd, warn=True).failed:
        make_work_dir_cmd = "mkdir -p {directory}".format(
            directory=directory)
        connection.run(make_work_dir_cmd)


@task
def deploy(_, env="dev"):
    config = load_config(env)
    work_dir = config["work_dir"]
    package_file_name = config["package_file_name"]
    system_python = config["system_python"]
    config_file_name = config["config_file_name"]

    connection = Connection(config["host"])
    connection.config.run.echo = True

    # 打包
    connection.local("python setup.py sdist")
    logging.info("【代码打包】OK")

    # 上传
    create_dir(connection, work_dir)
    upload(connection,
           "dist", package_file_name,
           work_dir, package_file_name)

    # 虚拟环境
    test_venv_cmd = "test -f {work_dir}/venv/bin/activate".format(
        work_dir=work_dir)
    if connection.run(test_venv_cmd, warn=True).failed:
        create_venv = "virtualenv -p {system_python} {work_dir}/venv".format(
            work_dir=work_dir, system_python=system_python)
        connection.run(create_venv)
        logging.info("【虚拟环境创建】OK")

    # 更新安装包
    install_requirements_cmd = "easy_install {package_file_name}".format(
        package_file_name=package_file_name,
        work_dir=work_dir)
    with connection.cd(work_dir):
        with connection.prefix(". venv/bin/activate"):
            connection.run(install_requirements_cmd)
    logging.info("【安装包更新】OK")

    # 配置上传
    upload(connection,
           "configure", config_file_name,
           work_dir, "config.py")
    upload(connection,
           ".", "uwsgi.ini",
           work_dir, "uwsgi.ini")

    # 服务启动 / 重启
    create_dir(connection, os.path.join(work_dir, "logs"))
    with connection.cd(work_dir):
        with connection.prefix(". venv/bin/activate"):
            check_service1_command = "autointerface check-service1"
            check_service2_command = "autointerface check-service2"
            start_service_command = "autointerface start"
            restart_service_command = "autointerface restart"
            if connection.run(check_service2_command, warn=True).failed:
                connection.run(start_service_command)
                action = "启动"
            else:
                connection.run(restart_service_command)
                action = "重启"

    # 成功确认
    with connection.cd(work_dir):
        with connection.prefix(". venv/bin/activate"):
            if connection.run(check_service1_command, warn=True).failed:
                logging.error("【%s】失败" % action)
            elif connection.run(check_service2_command, warn=True).failed:
                logging.error("【%s】失败" % action)
            else:
                logging.info("【%s】成功" % action)


@task
def migrate(_, env="dev"):
    config = load_config(env)
    work_dir = config["work_dir"]
    package_file_name = config["package_file_name"]
    system_python = config["system_python"]
    config_file_name = config["config_file_name"]

    connection = Connection(config["host"])
    connection.config.run.echo = True

    # 表结构的创建或更新
    with connection.cd(work_dir):
        with connection.prefix(". venv/bin/activate"):
            migrate_command = "migrate migrate"
            connection.run(migrate_command, warn=True)


@task
def rollback(_, env="dev"):
    config = load_config(env)
    work_dir = config["work_dir"]
    package_file_name = config["package_file_name"]
    system_python = config["system_python"]
    config_file_name = config["config_file_name"]

    connection = Connection(config["host"])
    connection.config.run.echo = True

    # 表结构的回滚
    with connection.cd(work_dir):
        with connection.prefix(". venv/bin/activate"):
            rollback_command = "migrate rollback"
            connection.run(rollback_command, warn=True)


@task
def init(_):
    if os.path.exists("fabric.ini"):
        logging.fatal("fabric.ini已存在，无法生成默认配置")
        sys.exit(-1)

    config = ConfigObj("fabric.ini", encoding='UTF-8')
    config["default"] = {}
    for key in config_dict:
        config["default"][key] = config_dict[key]
    config.write()
