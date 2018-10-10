
from peewee import *
from . import *


class Projects(MyModel):
    name = CharField(help_text='项目名称', null=False, unique=False, index=False)
    state = IntegerField(help_text='项目状态', default=1,
                         null=False, unique=False, index=False)
    description = TextField(help_text='项目描述', null=False,
                            unique=False, index=False)
