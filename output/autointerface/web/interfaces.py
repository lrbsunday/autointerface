

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
        "name": tools.get_params(request_info, 'name', need=True, vtype=str),
        "name_cn": tools.get_params(request_info, 'name_cn', need=True, vtype=str),
        "method": tools.get_params(request_info, 'method', need=True, vtype=str, choices=['GET', 'GETS', 'POST', 'PUT', 'DELETE']),
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


@interfaces_blueprint.route('/interfaces/<string:uid>', methods=['GET'])
@tools.request_decorator()
def get_one_interfaces(uid):
    uid = tools.check_params("uid", uid, vtype=int)

    try:
        row = Interfaces.select().where(Interfaces.uid == uid).get()
    except DoesNotExist:
        raise exceptions.ResourceNotFound(detail="接口%s不存在" % uid)

    return model_to_dict(row, recurse=True, backrefs=True)


@interfaces_blueprint.route('/interfaces/<string:uid>', methods=['DELETE'])
@tools.request_decorator()
def delete_interfaces(uid):
    uid = tools.check_params("uid", uid, vtype=int)

    q = Interfaces.delete().where(Interfaces.uid == uid)
    try:
        exec_code = q.execute()
    except IntegrityError as e:
        if e.args[0] in (1451, 1452):
            raise exceptions.ForeignConstraintException(detail="删除资源时，外键约束错误")
        else:
            raise exceptions.IntegrityError()
    if exec_code == 0:
        raise exceptions.ResourceNotFound(detail="删除接口%s不存在" % uid)

    return {}


@interfaces_blueprint.route('/interfaces/<string:uid>', methods=['PUT'])
@tools.request_decorator()
def create_or_update_interfaces(uid):
    uid = tools.check_params("uid", uid, vtype=int)
    request_info = request.get_json()

    fields = {}
    if "name" in request_info:
        fields["name"] = tools.get_params(
            request_info, 'name', need=False, vtype=str)
    if "name_cn" in request_info:
        fields["name_cn"] = tools.get_params(
            request_info, 'name_cn', need=False, vtype=str)
    if "method" in request_info:
        fields["method"] = tools.get_params(
            request_info, 'method', need=False, vtype=str)
    if "description" in request_info:
        fields["description"] = tools.get_params(
            request_info, 'description', need=False, vtype=str)
    if "recurse" in request_info:
        fields["recurse"] = tools.get_params(
            request_info, 'recurse', need=False, vtype=bool)
    if "backref" in request_info:
        fields["backref"] = tools.get_params(
            request_info, 'backref', need=False, vtype=bool)

    q = Interfaces.update(**fields).where(Interfaces.uid == uid)
    try:
        exec_code = q.execute()
    except IntegrityError as e:
        if e.args[0] == 1062:
            raise exceptions.ResourceAlreadyExists(detail="更新更新接口时，更新接口已存在")
        elif e.args[0] in (1451, 1452):
            raise exceptions.ForeignConstraintException(
                detail="更新更新接口时，外键约束错误")
        else:
            raise exceptions.IntegrityError()
    if exec_code == 0:
        raise exceptions.ResourceNotFound(detail="更新接口%s不存在" % uid)

    return {}


@interfaces_blueprint.route('/interfaces', methods=['GET'])
@tools.request_decorator()
def get_interfaces():
    filter_conditions = []
    sort_conditions = []

    name = tools.get_params(request.args, 'name', need=False, vtype=str)
    if name is not None:
        filter_conditions.append(Interfaces.name.startswith(name))

    method = tools.get_params(request.args, 'method', need=False, vtype=str, choices=[
                              'GET', 'GETS', 'POST', 'PUT', 'DELETE'])
    if method is not None:
        filter_conditions.append(Interfaces.method == method)

    project_id = tools.get_params(
        request.args, 'project_id', need=False, vtype=int)
    if project_id is not None:
        filter_conditions.append(Interfaces.project_id == project_id)

    s_name = tools.get_params(request.args, 's_name', need=False, vtype=str)
    if s_name is not None:
        if s_name == 'desc':
            sort_conditions.append(Interfaces.name.desc())
        else:
            sort_conditions.append(Interfaces.name)

    project_name = tools.get_params(
        request.args, 'project_name', need=False, vtype=str)
    if project_name is not None:
        filter_conditions.append(Projects.name == project_name)

    rows = Interfaces.select()
    rows = rows.join(Projects)
    if filter_conditions:
        rows = rows.where(*filter_conditions)
    if sort_conditions:
        rows = rows.order_by(*sort_conditions)

    return [model_to_dict(row, recurse=True, backrefs=True) for row in rows]
