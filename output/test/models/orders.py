
from peewee import *
from . import MyModel
from .resources import Resources


class Orders(MyModel):
    name = CharField(null=False, unique=True, index=True)
    state = IntegerField(default=1, null=False, unique=False, index=False)
    resource = ForeignKeyField(
        Resources, backref='orders', on_delete='CASCADE')
