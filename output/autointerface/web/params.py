

from flask import Blueprint, request
from peewee import DoesNotExist, IntegrityError
from playhouse.shortcuts import model_to_dict

from autointerface.models.params import Params
from autointerface.models.interfaces import Interfaces
from ..common import tools, exceptions

params_blueprint = Blueprint('params', __name__)


@params_blueprint.route('/params', methods=['POST'])
@tools.request_decorator()
def create_params():
    request_info = request.get_json()

    fields = {
        "name": tools.get_params(request_info, 'name', vtype=str, need=True),
        "description": tools.get_params(request_info, 'description', vtype=str, need=False),
        "need": tools.get_params(request_info, 'need', vtype=bool, need=True),
        "default": tools.get_params(request_info, 'default', need=False),
        "min": tools.get_params(request_info, 'min', vtype=int, need=False),
        "max": tools.get_params(request_info, 'max', vtype=int, need=False),
        "vtype": tools.get_params(request_info, 'vtype', vtype=str, need=False),
        "choices": tools.get_params(request_info, 'choices', vtype=list, need=False),
        "function": tools.get_params(request_info, 'function', vtype=str, default='normal', choices=['normal', 'filter', 'sort', 'page']),
        "filter_op": tools.get_params(request_info, 'filter_op', vtype=str, need=False),
        "filter_condition": tools.get_params(request_info, 'filter_condition', vtype=str, need=False),
        "interface_id": tools.get_params(request_info, 'interface_id', vtype=int, need=True),
    }

    try:
        row = Params.create(**fields)
    except IntegrityError as e:
        if e.args[0] == 1062:
            raise exceptions.ResourceAlreadyExists(detail="创建接口参数时，接口参数已存在")
        elif e.args[0] in (1451, 1452):
            raise exceptions.ForeignConstraintException(
                detail="创建接口参数时，外键约束错误")
        else:
            raise exceptions.IntegrityError()

    return {"id": row.uid}
