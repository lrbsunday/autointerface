
from peewee import *
from . import *


class Fields(MyModel):
    name = CharField(help_text='', null=False, unique=False, index=False)
    description = TextField(help_text='', default='',
                            null=False, unique=False, index=False)
    default = JSONField(help_text='', null=True, unique=False, index=False)
    type = CharField(help_text='', null=False, unique=False, index=False)
    null = BooleanField(help_text='', default=False,
                        null=False, unique=False, index=False)
    unique = BooleanField(help_text='', default=False,
                          null=False, unique=False, index=False)
    index = BooleanField(help_text='', default=False,
                         null=False, unique=False, index=False)
    foreign = IntegerField(help_text='', null=True, unique=False, index=False)
    on_delete = CharField(help_text='', null=True, unique=False, index=False)
    model = ForeignKeyField(Models, help_text='所属模型', null=False,
                            unique=False, index=False, on_delete='CASCADE', backref="fields")
