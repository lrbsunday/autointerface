

from flask import Blueprint, request
from peewee import DoesNotExist, IntegrityError
from playhouse.shortcuts import model_to_dict

from autointerface.models.projects import Projects
from ..common import tools, exceptions

projects_blueprint = Blueprint('projects', __name__)


@projects_blueprint.route('/projects', methods=['POST'])
@tools.request_decorator()
def create_projects():
    request_info = request.get_json()

    fields = {
        "name": tools.get_params(request_info, 'name', need=True, vtype=str),
        "state": tools.get_params(request_info, 'state', default=1, need=False, vtype=int),
        "description": tools.get_params(request_info, 'description', default='', need=False, vtype=str),
    }

    try:
        row = Projects.create(**fields)
    except IntegrityError as e:
        if e.args[0] == 1062:
            raise exceptions.ResourceAlreadyExists(detail="创建项目时，项目已存在")
        elif e.args[0] in (1451, 1452):
            raise exceptions.ForeignConstraintException(detail="创建项目时，外键约束错误")
        else:
            raise exceptions.IntegrityError()

    return {"id": row.uid}
