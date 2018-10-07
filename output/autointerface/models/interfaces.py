
from peewee import *
from . import *
from autointerface.models.projects import Projects


class Interfaces(MyModel):
    name = CharField(help_text='接口英文名称', null=False, unique=False, index=False)
    name_cn = CharField(help_text='接口中文名称', null=False,
                        unique=False, index=False)
    method = CharField(help_text='接口请求方法', null=False,
                       unique=False, index=False)
    description = TextField(help_text='描述信息', default='',
                            null=False, unique=False, index=False)
    project = ForeignKeyField(Projects, help_text='所属项目', null=False,
                              unique=False, index=False, on_delete='CASCADE', backref="interfaces")
    recurse = BooleanField(help_text='返回外键所指对象的内容，仅对查询类接口有效',
                           null=True, unique=False, index=False)
    backref = BooleanField(help_text='返回被作为外键的对象列表，仅对查询类接口有',
                           null=True, unique=False, index=False)
