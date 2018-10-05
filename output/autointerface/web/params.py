

from flask import Blueprint, request
from peewee import DoesNotExist, IntegrityError
from playhouse.shortcuts import model_to_dict

from autointerface.models.params import Params
from ..common import tools, exceptions

params_blueprint = Blueprint('params', __name__)


@params_blueprint.route('/params', methods=['POST'])
@tools.request_decorator()
def create_params():
    request_info = request.get_json()

    fields = {
        "name": tools.get_params(request_info, 'name', need=True, vtype=str),
        "description": tools.get_params(request_info, 'description', need=False, default='', vtype=str),
        "need": tools.get_params(request_info, 'need', need=False, default=True, vtype=bool),
        "default": tools.get_params(request_info, 'default', need=False),
        "min": tools.get_params(request_info, 'min', need=False, vtype=int),
        "max": tools.get_params(request_info, 'max', need=False, vtype=int),
        "vtype": tools.get_params(request_info, 'vtype', need=False, vtype=str),
        "choices": tools.get_params(request_info, 'choices', need=False, vtype=list),
        "function": tools.get_params(request_info, 'function', need=False, default='normal', choices=['normal', 'filter', 'sort', 'page'], vtype=str),
        "filter_op": tools.get_params(request_info, 'filter_op', need=False, vtype=str),
        "filter_condition": tools.get_params(request_info, 'filter_condition', need=False, vtype=str),
        "interface_id": tools.get_params(request_info, 'interface_id', need=True, vtype=int),
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
