
from peewee import *
from . import *


class Projects(MyModel):
    name = CharField(help_text='项目名称', null=False, unique=True, index=True)
    state = IntegerField(help_text='状态，1在线、2下线', default=1,
                         null=False, unique=False, index=False)
    description = TextField(help_text='描述信息', default='',
                            null=False, unique=False, index=False)
