import json
import logging
import traceback
from flask import Flask, request
from werkzeug.exceptions import MethodNotAllowed

from ..models import database
from ..common import exceptions
from .orders import orders_blueprint
from .resources import resources_blueprint

app = Flask(__name__)

logger = logging.getLogger('interface')


@app.before_request
def before_request():
    database.connect()


@app.errorhandler(exceptions.MyBaseException)
def my_exception(e):
    r_dict = {"code": e.code, "message": e.message, "detail": e.detail}
    r_str = json.dumps(r_dict)
    logger.exception("接口调用发生已知异常：%s" % r_str)
    return r_str


@app.errorhandler(Exception)
def unknown_exception(e):
    if isinstance(e, MethodNotAllowed):
        detail = "接口地址为%s，请求方法为%s" % (request.base_url, request.method)
        r_dict = {"code": 405, "message": "请求方法不存在", "detail": detail}
        r_str = json.dumps(r_dict)
        logger.error("接口调用发生已知异常：%s" % detail)
    else:
        detail = traceback.format_exc()
        r_dict = {"code": 500, "message": "未知异常", "detail": detail}
        r_str = json.dumps(r_dict)
        logger.error("接口调用发生未知异常：%s" % detail)
    return r_str


@app.errorhandler(404)
def path_not_found(_):
    detail = "接口地址为%s" % request.base_url
    r_dict = {"code": 404, "message": "接口地址不存在", "detail": detail}
    r_str = json.dumps(r_dict)
    logger.error("接口地址不存在：%s" % detail)
    return r_str


@app.teardown_request
def teardown_request(_):
    if not database.is_closed():
        database.close()


app.register_blueprint(orders_blueprint, url_prefix='/api/v1')
app.register_blueprint(resources_blueprint, url_prefix='/api/v1')
