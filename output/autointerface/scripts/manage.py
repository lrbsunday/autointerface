import os
import subprocess
import logging
import sys
import json
import time
import functools

import click
import requests
from configobj import ConfigObj

sys.path.append(os.getcwd())
import config

os.environ["PATH"] = os.environ["PATH"] + \
    ":/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/usr/local/bin"
pid_file_name = "pidfile"
uwsgi_config_file_name = "uwsgi.ini"
uwsgi_config = {}
env = config.env
devnull = open("/dev/null")

logging.basicConfig(level=logging.INFO,
                    format='%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def __load_ini_config(env, config_file_name):
    config_dict = {
        "http": "localhost:8080"
    }
    try:
        config = ConfigObj(config_file_name, file_error=True, encoding='UTF-8')
    except IOError:
        logging.fatal("配置文件%s不存在" % config_file_name)
        sys.exit(-1)
    except SyntaxError as e:
        logging.fatal("配置%s存在错误: %s" % (config_file_name, str(e)))
        sys.exit(-1)
    else:
        if env not in config:
            logging.fatal("%s不存在名为%s的区块" % (config_file_name, env))
            sys.exit(-1)
        for key in config_dict:
            if key not in config[env]:
                logging.fatal("%s中%s区块的%s字段不存在" % (config_file_name, env, key))
                sys.exit(-1)
            config_dict[key] = config[env][key]
    return config_dict


def check_until(expect, max_retry_count=5):

    def __decorator__(func):

        @functools.wraps(func)
        def __wrapper__(*args, **kwargs):
            retry_count = -1
            while True:
                retry_count += 1
                if retry_count > max_retry_count:
                    return not expect

                if retry_count > 0:
                    time.sleep(1)

                if expect == func(*args, **kwargs):
                    return expect

        return __wrapper__

    return __decorator__


def get_pid():
    try:
        fp = open(pid_file_name)
    except IOError:
        logging.fatal("{pid_file_name}文件不存在".format(
            pid_file_name=pid_file_name))
        sys.exit(-1)
    pid = fp.readline()
    return pid.strip()


def __check_service1():
    url = "http://%s/_status" % uwsgi_config["http"]
    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException:
        logging.error("接口请求失败 - %s" % url)
        return False

    if response.status_code != 200:
        logging.error("接口请求失败(%s) - %s" % (response.status_code, url))
        return False

    try:
        r_dict = json.loads(response.text)
    except ValueError:
        logging.error("接口返回结果解析失败 - %s" % response.text)
        return False

    if "code" not in r_dict or r_dict["code"] != 200:
        logging.error("接口状态码异常(%s) - %s" % (
            r_dict.get("code"), r_dict.get("message")))
        return False

    return r_dict['data']['status']


def __check_service2():
    pid = get_pid()
    if ":" in uwsgi_config["http"]:
        port = uwsgi_config["http"].split(":")[-1]
    else:
        port = "80"

    cmd = "test \"`lsof -i:{port}|awk '$2=={pid}{{print $2}}'`\" == {pid}".format(
        port=port, pid=pid)
    logging.debug(cmd)
    ret = os.system(cmd)
    if ret == 0:
        return True
    else:
        return False


def __check_port():
    if ":" in uwsgi_config["http"]:
        port = uwsgi_config["http"].split(":")[-1]
    else:
        port = "80"

    cmd = "lsof -i:{port}".format(port=port)
    logging.debug(cmd)
    ret = os.system(cmd)
    if ret == 0:
        return True
    else:
        return False


def __check_process():
    pid = get_pid()

    cmd = "test \"`ps -ef|awk '$2=={pid}{{ print $2}}'`\" == {pid}".format(
        pid=pid)
    logging.debug(cmd)
    ret = os.system(cmd)
    if ret == 0:
        return True
    else:
        return False


@click.group()
def main():
    global uwsgi_config
    uwsgi_config = __load_ini_config(env, uwsgi_config_file_name)


@main.command()
def check_service1():
    ret = __check_service1()
    if ret:
        logging.info("服务已启动")
    else:
        logging.info("服务已停止")
        sys.exit(-1)


@main.command()
def check_service2():
    ret = __check_service2()
    if ret:
        logging.info("服务已启动")
    else:
        logging.info("服务已停止")
        sys.exit(-1)


@main.command()
def check_port():
    ret = __check_port()
    if ret:
        logging.info("端口开放中")
    else:
        logging.info("端口已关闭")
        sys.exit(-1)


@main.command()
def check_process():
    ret = __check_process()
    if ret:
        logging.info("进程已启动")
    else:
        logging.info("进程已停止")
        sys.exit(-1)


@main.command()
def start():
    if __check_service2():
        logging.fatal("服务已启用，不要重复操作！")
        sys.exit(-1)
    if __check_port():
        logging.fatal("端口被占用！")
        sys.exit(-1)
    args = 'uwsgi --ini {uwsgi_config_file_name}:{env}'.format(
        uwsgi_config_file_name=uwsgi_config_file_name,
        env=env).split()
    ret = subprocess.Popen(args, stdout=devnull).wait()
    if ret == 0 and check_until(True, max_retry_count=5)(__check_service1)() \
            and check_until(True, max_retry_count=5)(__check_service2)():
        logging.info("服务启动成功")
    else:
        logging.error("服务启动失败")
        sys.exit(-1)


@main.command()
def stop():
    if not __check_service2():
        logging.fatal("服务未启动，不要重复操作！")
        sys.exit(-1)
    args = 'uwsgi --stop {pid_file_name}'.format(
        pid_file_name=pid_file_name).split()
    ret = subprocess.Popen(args, stdout=devnull).wait()
    if ret == 0 and not check_until(False, max_retry_count=5)(__check_port)() \
            and not check_until(False, max_retry_count=5)(__check_process)():
        logging.info("服务停止成功")
    else:
        logging.error("服务停止失败")
        sys.exit(-1)


@main.command()
def restart():
    if not __check_service2():
        logging.fatal("服务未启动，无法重启！")
        sys.exit(-1)
    args = 'uwsgi --reload {}'.format(pid_file_name).split()
    ret = subprocess.Popen(args, stdout=devnull).wait()
    if ret == 0 and check_until(True, max_retry_count=5)(__check_service1)() \
            and check_until(True, max_retry_count=5)(__check_service2)():
        logging.info("服务重启成功")
    else:
        logging.error("服务重启失败")
        sys.exit(-1)
