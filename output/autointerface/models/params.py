
from peewee import *
from . import *
from autointerface.models.interfaces import Interfaces
from autointerface.models.fields import Fields


class Params(MyModel):
    name = CharField(help_text='', null=False, unique=False, index=False)
    description = TextField(help_text='', null=False,
                            unique=False, index=False)
    need = BooleanField(help_text='', default=True,
                        null=False, unique=False, index=False)
    default = JSONField(help_text='', null=True, unique=False, index=False)
    min = IntegerField(help_text='', null=True, unique=False, index=False)
    max = IntegerField(help_text='', null=True, unique=False, index=False)
    vtype = CharField(help_text='', null=True, unique=False, index=False)
    function = CharField(help_text='', default='normal',
                         null=False, unique=False, index=False)
    filter_op = CharField(help_text='', null=True, unique=False, index=False)
    filter_condition = CharField(
        help_text='', null=True, unique=False, index=False)
    interface = ForeignKeyField(Interfaces, help_text='所属接口', null=False,
                                unique=False, index=False, on_delete='CASCADE', backref="params")
    choices = JSONField(help_text='可选值', null=True, unique=False, index=False)
    field = ForeignKeyField(Fields, help_text='', null=True, unique=False,
                            index=False, on_delete='CASCADE', backref="params")
