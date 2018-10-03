

from flask import Blueprint, request
from peewee import DoesNotExist, IntegrityError
from playhouse.shortcuts import model_to_dict

from test.models.orders import Orders
from test.models.resources import Resources
from ..common import tools, exceptions

orders_blueprint = Blueprint('orders', __name__)


@orders_blueprint.route('/orders', methods=['GET'])
@tools.request_decorator()
def get_orders():
    filter_conditions = []
    sort_conditions = []

    page = tools.get_params(request.args, 'page',
                            need=False, default=1, min=1, max=3, vtype=int)

    size = tools.get_params(request.args, 'size',
                            need=False, default=10, vtype=int)

    name = tools.get_params(request.args, 'name', need=False, vtype=str)
    if name is not None:
        filter_conditions.append(Orders.name == name)

    s_name = tools.get_params(request.args, 's_name',
                              need=False, vtype=str, choices=['desc', 'asc'])
    if s_name is not None:
        if s_name == 'desc':
            sort_conditions.append(Orders.name.desc())
        else:
            sort_conditions.append(Orders.name)

    resource_name = tools.get_params(
        request.args, 'resource_name', need=False, vtype=str)
    if resource_name is not None:
        filter_conditions.append(Resources.name == resource_name)

    s_resource_name = tools.get_params(
        request.args, 's_resource_name', need=False, vtype=str, choices=['desc', 'asc'])
    if s_resource_name is not None:
        if s_resource_name == 'desc':
            sort_conditions.append(Resources.name.desc())
        else:
            sort_conditions.append(Resources.name)

    rows = Orders.select()
    rows = rows.join(Resources)
    if filter_conditions:
        rows = rows.where(*filter_conditions)
    if sort_conditions:
        rows = rows.order_by(*sort_conditions)

    rows = rows.paginate(page=page, paginate_by=size)
    return [model_to_dict(row, recurse=True, backrefs=True) for row in rows]


@orders_blueprint.route('/orders/<string:uid>', methods=['GET'])
@tools.request_decorator()
def get_one_orders(uid):
    uid = tools.check_params("uid", uid, vtype=int)

    try:
        row = Orders.select().where(Orders.uid == uid).get()
    except DoesNotExist:
        raise exceptions.ResourceNotFound(detail="订单%s不存在" % uid)

    return model_to_dict(row, recurse=False, backrefs=False)


@orders_blueprint.route('/orders', methods=['POST'])
@tools.request_decorator()
def create_orders():
    request_info = request.get_json()

    fields = {
        "name": tools.get_params(request_info, 'name', need=True, vtype=str),
        "state": tools.get_params(request_info, 'state', need=False, default=1, vtype=int),
        "resource_id": tools.get_params(request_info, 'resource_id', need=True, vtype=int),
    }

    try:
        row = Orders.create(**fields)
    except IntegrityError as e:
        if e.args[0] == 1062:
            raise exceptions.ResourceAlreadyExists(detail="创建订单时，订单已存在")
        elif e.args[0] in (1451, 1452):
            raise exceptions.ForeignConstraintException(detail="创建订单时，外键约束错误")
        else:
            raise exceptions.IntegrityError()

    return {"id": row.uid}


@orders_blueprint.route('/orders/<string:uid>', methods=['PUT'])
@tools.request_decorator()
def create_or_update_orders(uid):
    uid = tools.check_params("uid", uid, vtype=int)
    request_info = request.get_json()

    fields = {}
    if "name" in request_info:
        fields["name"] = tools.get_params(
            request_info, 'name', need=False, vtype=str)
    if "state" in request_info:
        fields["state"] = tools.get_params(
            request_info, 'state', need=False, default=1, vtype=int)
    if "resource_id" in request_info:
        fields["resource_id"] = tools.get_params(
            request_info, 'resource_id', need=False, vtype=int)

    q = Orders.update(**fields).where(Orders.uid == uid)
    try:
        exec_code = q.execute()
    except IntegrityError as e:
        if e.args[0] == 1062:
            raise exceptions.ResourceAlreadyExists(detail="更新订单时，订单已存在")
        elif e.args[0] in (1451, 1452):
            raise exceptions.ForeignConstraintException(detail="更新订单时，外键约束错误")
        else:
            raise exceptions.IntegrityError()
    if exec_code == 0:
        raise exceptions.ResourceNotFound(detail="订单%s不存在" % uid)

    return {}


@orders_blueprint.route('/orders/<string:uid>', methods=['DELETE'])
@tools.request_decorator()
def delete_orders(uid):
    uid = tools.check_params("uid", uid, vtype=int)

    q = Orders.delete().where(Orders.uid == uid)
    try:
        exec_code = q.execute()
    except IntegrityError as e:
        if e.args[0] in (1451, 1452):
            raise exceptions.ForeignConstraintException(detail="删除资源时，外键约束错误")
        else:
            raise exceptions.IntegrityError()
    if exec_code == 0:
        raise exceptions.ResourceNotFound(detail="订单%s不存在" % uid)

    return {}
