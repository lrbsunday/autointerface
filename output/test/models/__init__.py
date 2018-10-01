import datetime

from peewee import MySQLDatabase, Model
from peewee import PrimaryKeyField, DateTimeField

from test import config

database = MySQLDatabase(config.dbname,
                         host=config.host,
                         port=config.port,
                         user=config.username,
                         password=config.password)


class MyModel(Model):
    uid = PrimaryKeyField(db_column='uid')
    create_time = DateTimeField(
        db_column='create_time', default=datetime.datetime.now)
    update_time = DateTimeField(
        db_column='update_time', default=datetime.datetime.now)

    class Meta:
        database = database

    @classmethod
    def update(cls, **update):
        update['update_time'] = datetime.datetime.now()
        return super(MyModel, cls).update(**update)
