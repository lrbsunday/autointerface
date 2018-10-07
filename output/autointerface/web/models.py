

from flask import Blueprint, request
from peewee import DoesNotExist, IntegrityError, fn
from playhouse.shortcuts import model_to_dict

from autointerface.models.models import Models
from ..common import tools, exceptions

models_blueprint = Blueprint('models', __name__)


@models_blueprint.route('/models', methods=['POST'])
@tools.request_decorator()
def create_models():
    request_info = request.get_json()

    fields = {
        "name": tools.get_params(request_info, 'name', need=True, vtype=str),
        "name_cn": tools.get_params(request_info, 'name_cn', need=True, vtype=str),
        "description": tools.get_params(request_info, 'description', need=False, default='', vtype=str),
        "project_id": tools.get_params(request_info, 'project_id', need=True, vtype=int),
    }

    try:
        row = Models.create(**fields)
    except IntegrityError as e:
        if e.args[0] == 1062:
            raise exceptions.ResourceAlreadyExists(detail="创建模型时，模型已存在")
        elif e.args[0] in (1451, 1452):
            raise exceptions.ForeignConstraintException(detail="创建模型时，外键约束错误")
        else:
            raise exceptions.IntegrityError()

    return {"id": row.uid}
