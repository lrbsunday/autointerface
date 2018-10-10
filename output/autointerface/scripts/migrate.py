""" 表结构发生变化时，做数据迁移 """
import subprocess
import logging

import click
from peewee_migrate import Router

from autointerface import models, config


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
def cli():
    pass


@cli.command()
def migrate():
    router = Router(models.database, ignore=[models.MyModel])
    router.create(auto=models)

    backup(router.todo[-1])
    router.run()


@cli.command()
def rollback():
    router = Router(models.database, ignore=[models.MyModel])
    if not router.done:
        logging.warning("没有migrate记录，无法回滚")
    name = router.done[-1]
    router.rollback(name)

    command = "rm migrations/{name}.py migrations/{name}.data".format(
        name=name)
    subprocess.Popen(command.split(" ")).wait()


cli.add_command(migrate)
cli.add_command(rollback)
cli()
