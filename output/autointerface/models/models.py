
from peewee import *
from . import *


class Models(MyModel):
    name = CharField(help_text='模型英文名称', null=False, unique=False, index=False)
    name_cn = CharField(help_text='模型中文名称', null=False,
                        unique=False, index=False)
    description = TextField(help_text='模型描述', default='',
                            null=False, unique=False, index=False)
    project = ForeignKeyField(Projects, help_text='所属项目', null=False,
                              unique=False, index=False, on_delete='CASCADE', backref="models")
