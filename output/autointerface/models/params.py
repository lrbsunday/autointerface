
from peewee import *
from . import *
from autointerface.models.interfaces import Interfaces


class Params(MyModel):
    name = CharField(help_text='参数名称', null=False, unique=False, index=False)
    description = TextField(help_text='参数描述信息', default='',
                            null=False, unique=False, index=False)
    need = BooleanField(help_text='是否必填', default=False,
                        null=False, unique=False, index=False)
    default = JSONField(help_text='默认值', null=True, unique=False, index=False)
    min = IntegerField(help_text='最小值', null=True, unique=False, index=False)
    max = IntegerField(help_text='最大值', null=True, unique=False, index=False)
    choices = JSONField(help_text='可选值', null=True, unique=False, index=False)
    vtype = CharField(help_text='参数类型', null=True, unique=False, index=False)
    function = CharField(help_text='参数用途，filter、sort、page',
                         null=False, unique=False, index=False)
    filter_op = CharField(help_text='过滤专用，表示过滤操作符',
                          null=True, unique=False, index=False)
    filter_condition = CharField(
        help_text='过滤专用，表示过滤条件', null=True, unique=False, index=False)
    interface = ForeignKeyField(
        Interfaces, help_text='接口外键', null=False, on_delete='CASCADE', backref="params")
