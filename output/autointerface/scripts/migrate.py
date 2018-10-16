""" 表结构发生变化时，做数据迁移 """
import subprocess
import logging
import sys

import click
from peewee_migrate import Router

from autointerface import models, config


logging.basicConfig(level=logging.INFO,
                    format='%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def backup(name):
    command = """
        mysqldump -t -h %s -P %s -u %s -p %s --password=%s
    """ % (config.host, config.port, config.username,
           config.dbname, config.password)
    filename = "migrations/{name}.data".format(name=name)
    with open(filename, "w") as fp:
        subprocess.Popen(command.strip().split(" "),
                         stdout=fp).wait()


@click.group()
def main():
    pass


@main.command()
@click.option('--name', default=None, help='指定迁移脚本名称，否则自动生成')
def migrate(name):
    router = Router(models.database, ignore=[models.MyModel])

    if name is None:
        router.create(auto=models)
        name = router.todo[-1]

    try:
        backup(name)
        router.run()
    except:
        logging.exception("migrate失败")
        clean(name, backup_py=True)
        sys.exit(-1)


@main.command()
def rollback():
    try:
        router = Router(models.database, ignore=[models.MyModel])
        if not router.done:
            logging.warning("没有migrate记录，无法回滚")
            sys.exit(-1)

        name = router.done[-1]
        router.rollback(name)

        clean(name)
    except:
        logging.exception("rollback失败")
        sys.exit(-1)


def clean(name, backup_py=False):
    if backup_py:
        name_manuel = name.replace("auto", "manuel")
        command = "cp migrations/{name}.py migrations/{name_manuel}.py".format(
            name=name, name_manuel=name_manuel)
        subprocess.Popen(command.split(" ")).wait()

    command = "rm migrations/{name}.py migrations/{name}.data".format(
        name=name)
    subprocess.Popen(command.split(" ")).wait()
