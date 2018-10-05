
from peewee import *
from . import *
from autointerface.models.models import Models


class Fields(MyModel):
    name = CharField(help_text='英文名称', null=False, unique=False, index=False)
    description = TextField(help_text='描述信息', default='',
                            null=False, unique=False, index=False)
    default = JSONField(help_text='默认值', null=True, unique=False, index=False)
    type = CharField(help_text='类型', null=False, unique=False, index=False)
    null = BooleanField(help_text='可否为空', default=True,
                        null=False, unique=False, index=False)
    unique = BooleanField(help_text='是否唯一', default=False,
                          null=False, unique=False, index=False)
    index = BooleanField(help_text='可否索引', default=False,
                         null=False, unique=False, index=False)
    foreign = IntegerField(help_text='外键专用，表示是谁的外键',
                           null=True, unique=False, index=False)
    on_delete = CharField(
        help_text='外键专用，表示删除时的行为。CASCADE表示递归删除，参考peewee文档', null=True, unique=False, index=False)
    model = ForeignKeyField(Models, help_text='模型外键',
                            null=False, on_delete='CASCADE')
