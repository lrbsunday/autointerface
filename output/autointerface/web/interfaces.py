

from flask import Blueprint, request
from peewee import DoesNotExist, IntegrityError
from playhouse.shortcuts import model_to_dict

from autointerface.models.interfaces import Interfaces
from ..common import tools, exceptions

interfaces_blueprint = Blueprint('interfaces', __name__)


@interfaces_blueprint.route('/interfaces', methods=['POST'])
@tools.request_decorator()
def create_interfaces():
    request_info = request.get_json()

    fields = {
        "name": tools.get_params(request_info, 'name', need=True, vtype=str),
        "name_cn": tools.get_params(request_info, 'name_cn', need=True, vtype=str),
        "method": tools.get_params(request_info, 'method', need=True, choices=['GET', 'GETS', 'POST', 'PUT', 'DELETE'], vtype=str),
        "description": tools.get_params(request_info, 'description', need=False, default='', vtype=str),
        "project_id": tools.get_params(request_info, 'project_id', need=True, vtype=int),
        "recurse": tools.get_params(request_info, 'recurse', need=False, vtype=bool),
        "backref": tools.get_params(request_info, 'backref', need=False, vtype=bool),
    }

    try:
        row = Interfaces.create(**fields)
    except IntegrityError as e:
        if e.args[0] == 1062:
            raise exceptions.ResourceAlreadyExists(detail="创建接口时，接口已存在")
        elif e.args[0] in (1451, 1452):
            raise exceptions.ForeignConstraintException(detail="创建接口时，外键约束错误")
        else:
            raise exceptions.IntegrityError()

    return {"id": row.uid}
