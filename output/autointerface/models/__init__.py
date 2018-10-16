import datetime
import json

from peewee import MySQLDatabase, Model, Field
from peewee import PrimaryKeyField, DateTimeField, IntegerField

from autointerface import config

database = MySQLDatabase(config.dbname,
                         host=config.host,
                         port=config.port,
                         user=config.username,
                         password=config.password)


class MyModel(Model):
    uid = PrimaryKeyField(db_column='uid')
    version = IntegerField(db_column='version', null=True, default=1)
    create_time = DateTimeField(
        db_column='create_time', default=datetime.datetime.now)
    update_time = DateTimeField(
        db_column='update_time', default=datetime.datetime.now)

    class Meta:
        database = database

    @classmethod
    def update(cls, **update):
        version = None
        if 'version' in update:
            version = update['version']
        update['update_time'] = datetime.datetime.now()
        update['version'] = cls.version + 1
        q = super(MyModel, cls).update(**update)
        print(version)
        if version is None:
            return q
        else:
            return q.where(cls.version == version)


class JSONField(Field):
    field_type = 'json'

    def db_value(self, value):
        return json.dumps(value)

    def python_value(self, value):
        return json.loads(value)
