

from flask import Blueprint, request
from peewee import DoesNotExist, IntegrityError
from playhouse.shortcuts import model_to_dict

from ..models.resources import Resources
from ..common import tools, exceptions

resources_blueprint = Blueprint('resources', __name__)


@resources_blueprint.route('/resources', methods=['GET'])
@tools.request_decorator()
def get_resources():
    filter_conditions = []
    sort_conditions = []

    page = tools.get_params(request.args, 'page',
                            need=False, default=1, vtype=int)

    size = tools.get_params(request.args, 'size',
                            need=False, default=10, vtype=int)

    name = tools.get_params(request.args, 'name', need=False, vtype=str)
    if name is not None:
        filter_conditions.append(Resources.name == name)

    s_name = tools.get_params(request.args, 's_name',
                              need=False, vtype=str, choices=['desc', 'asc'])
    if s_name is not None:
        if s_name == 'desc':
            sort_conditions.append(Resources.name.desc())
        else:
            sort_conditions.append(Resources.name)

    rows = Resources.select()
    if filter_conditions:
        rows = rows.where(*filter_conditions)
    if sort_conditions:
        rows = rows.order_by(*sort_conditions)

    rows = rows.paginate(page=page, paginate_by=size)
    return [model_to_dict(row, recurse=True, backrefs=True) for row in rows]


@resources_blueprint.route('/resources/<string:uid>', methods=['GET'])
@tools.request_decorator()
def get_one_resources(uid):
    uid = tools.check_params("uid", uid, vtype=int)

    try:
        row = Resources.select().where(Resources.uid == uid).get()
    except DoesNotExist:
        raise exceptions.ResourceNotFound(detail="资源%s不存在" % uid)

    return model_to_dict(row, recurse=False, backrefs=False)


@resources_blueprint.route('/resources', methods=['POST'])
@tools.request_decorator()
def create_resources():
    request_info = request.get_json()

    fields = {
        "name": tools.get_params(request_info, 'name', need=True, vtype=str),
        "state": tools.get_params(request_info, 'state', need=False, default=1, vtype=int),
    }

    try:
        row = Resources.create(**fields)
    except IntegrityError as e:
        if e.args[0] == 1062:
            raise exceptions.ResourceAlreadyExists(detail="创建资源时，资源已存在")
        elif e.args[0] in (1451, 1452):
            raise exceptions.ForeignConstraintException(detail="创建资源时，外键约束错误")
        else:
            raise exceptions.IntegrityError()

    return {"id": row.uid}


@resources_blueprint.route('/resources/<string:uid>', methods=['PUT'])
@tools.request_decorator()
def create_or_update_resources(uid):
    uid = tools.check_params("uid", uid, vtype=int)
    request_info = request.get_json()

    fields = {}
    if "name" in request_info:
        fields["name"] = tools.get_params(
            request_info, 'name', need=False, vtype=str)
    if "state" in request_info:
        fields["state"] = tools.get_params(
            request_info, 'state', need=False, default=1, vtype=int)

    q = Resources.update(**fields).where(Resources.uid == uid)
    try:
        exec_code = q.execute()
    except IntegrityError as e:
        if e.args[0] == 1062:
            raise exceptions.ResourceAlreadyExists(detail="更新资源时，资源已存在")
        elif e.args[0] in (1451, 1452):
            raise exceptions.ForeignConstraintException(detail="更新资源时，外键约束错误")
        else:
            raise exceptions.IntegrityError()
    if exec_code == 0:
        raise exceptions.ResourceNotFound(detail="资源%s不存在" % uid)

    return {}


@resources_blueprint.route('/resources/<string:uid>', methods=['DELETE'])
@tools.request_decorator()
def delete_resources(uid):
    uid = tools.check_params("uid", uid, vtype=int)

    q = Resources.delete().where(Resources.uid == uid)
    try:
        exec_code = q.execute()
    except IntegrityError as e:
        if e.args[0] in (1451, 1452):
            raise exceptions.ForeignConstraintException(detail="删除资源时，外键约束错误")
        else:
            raise exceptions.IntegrityError()
    if exec_code == 0:
        raise exceptions.ResourceNotFound(detail="资源%s不存在" % uid)

    return {}
