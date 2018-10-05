

from flask import Blueprint, request
from peewee import DoesNotExist, IntegrityError
from playhouse.shortcuts import model_to_dict

from autointerface.models.interfaces import Interfaces
from autointerface.models.projects import Projects
from ..common import tools, exceptions

interfaces_blueprint = Blueprint('interfaces', __name__)


@interfaces_blueprint.route('/interfaces', methods=['POST'])
@tools.request_decorator()
def create_interfaces():
    request_info = request.get_json()

    fields = {
        "name": tools.get_params(request_info, 'name', vtype=str, need=True),
        "name_cn": tools.get_params(request_info, 'name_cn', vtype=str, need=True),
        "method": tools.get_params(request_info, 'method', choices=['GET', 'GETS', 'POST', 'PUT', 'DELETE'], vtype=str, need=True),
        "description": tools.get_params(request_info, 'description', default='', vtype=str, need=False),
        "project_id": tools.get_params(request_info, 'project_id', vtype=int, need=True),
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
