import json
import datetime
import functools

from .exceptions import ParamsException


class DefaultEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")


def request_decorator():
    def __wrapper__(func):
        @functools.wraps(func)
        def __wrapper2__(*args, **kwargs):
            r_dict = {
                "code": 200,
                "message": "成功",
                "data": func(*args, **kwargs)
            }
            return json.dumps(r_dict, cls=DefaultEncoder)

        return __wrapper2__

    return __wrapper__


def get_params(request_info, key, default=None, vtype=None,
               need=False,
               choices=None, min=None, max=None):
    value = request_info.get(key, default)
    return check_params(key, value, need=need, vtype=vtype,
                        choices=choices, min=min, max=max)


def check_params(key, value, need=False, vtype=None,
                 choices=None, min=None, max=None):
    if need and value is None:
        raise ParamsException(detail="参数%s不能为空" % key)

    if value is None:
        return value

    if vtype is not None and not isinstance(value, vtype):
        try:
            value = vtype(value)
        except ValueError:
            raise ParamsException(
                detail="参数%s的类型不是%s" % (key, vtype.__name__))

    if choices is not None and value not in choices:
        raise ParamsException(
            detail="参数%s的值%s不在%s中" % (key, value, repr(choices)))

    if min is not None:
        if isinstance(value, (int, float)) and value < min:
            raise ParamsException(
                detail="参数%s的值%s不能小于%s" % (key, value, min))
        if isinstance(value, (str, list)) and len(value) < min:
            raise ParamsException(
                detail="参数%s的长度%s不能小于%s" % (key, len(value), min))

    if max is not None:
        if isinstance(value, (int, float)) and value > max:
            raise ParamsException(
                detail="参数%s的值%s不能大于%s" % (key, value, max))
        if isinstance(value, (str, list)) and len(value) > max:
            raise ParamsException(
                detail="参数%s的长度%s不能大于%s" % (key, len(value), max))

    return value
