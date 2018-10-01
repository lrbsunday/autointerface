
from peewee import *
from . import MyModel


class Resources(MyModel):
    name = CharField(null=False, unique=True, index=True)
    state = IntegerField(default=1, null=False, unique=False, index=False)
