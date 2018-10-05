
from peewee import *
from . import *
from autointerface.models.projects import Projects


class Models(MyModel):
    name = CharField(help_text='模型英文名称', null=False, unique=False, index=False)
    name_cn = CharField(help_text='模型中文名称', null=False,
                        unique=False, index=False)
    description = TextField(help_text='描述信息', default='',
                            null=False, unique=False, index=False)
    project = ForeignKeyField(
        Projects, help_text='项目外键', null=False, on_delete='CASCADE', backref="models")
