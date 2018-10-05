

from flask import Blueprint, request
from peewee import DoesNotExist, IntegrityError
from playhouse.shortcuts import model_to_dict

from autointerface.models.fields import Fields
from ..common import tools, exceptions

fields_blueprint = Blueprint('fields', __name__)


@fields_blueprint.route('/fields', methods=['POST'])
@tools.request_decorator()
def create_fields():
    request_info = request.get_json()

    fields = {
        "name": tools.get_params(request_info, 'name', need=True, vtype=str),
        "description": tools.get_params(request_info, 'description', need=False, default='', vtype=str),
        "default": tools.get_params(request_info, 'default', need=False),
        "type": tools.get_params(request_info, 'type', need=True, vtype=str),
        "null": tools.get_params(request_info, 'null', need=False, default=False, vtype=bool),
        "unique": tools.get_params(request_info, 'unique', need=False, default=False, vtype=bool),
        "index": tools.get_params(request_info, 'index', need=False, default=False, vtype=bool),
        "foreign": tools.get_params(request_info, 'foreign', need=False, vtype=int),
        "on_delete": tools.get_params(request_info, 'on_delete', need=False, vtype=str),
        "model_id": tools.get_params(request_info, 'model_id', need=True, vtype=int),
    }

    try:
        row = Fields.create(**fields)
    except IntegrityError as e:
        if e.args[0] == 1062:
            raise exceptions.ResourceAlreadyExists(detail="创建模型字段时，模型字段已存在")
        elif e.args[0] in (1451, 1452):
            raise exceptions.ForeignConstraintException(
                detail="创建模型字段时，外键约束错误")
        else:
            raise exceptions.IntegrityError()

    return {"id": row.uid}
