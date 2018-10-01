import logging


def format_value(value):
    if isinstance(value, int):
        return repr(value)
    elif isinstance(value, float):
        return repr(round(value, 4))
    elif isinstance(value, bool):
        return repr(value)
    elif isinstance(value, str):
        return repr(value)
    elif isinstance(value, list):
        return repr(value)
    else:
        logging.error("类型%s未知，无法格式化" % type(value))
        return 'unknown'


def format_param_type(vtype):
    if vtype == 'integer':
        return 'int'
    elif vtype == 'string':
        return 'str'
    elif vtype == 'float':
        return 'float'
    elif vtype == 'bool':
        return 'bool'
    else:
        logging.error("接口定义的类型%s不支持" % vtype)
        return 'unknown'


def format_model_type(vtype):
    if vtype == 'integer':
        return 'IntegerField'
    elif vtype == 'bigint':
        return 'BigIntegerField'
    elif vtype == 'string':
        return 'CharField'
    elif vtype == 'text':
        return 'TextField'
    elif vtype == 'float':
        return 'FloatField'
    elif vtype == 'bool':
        return 'BooleanField'
    elif vtype == 'datetime':
        return 'DateTimeField'
    elif vtype == 'foreign':
        return 'ForeignKeyField'
    else:
        logging.error("模型定义的类型%s不支持" % vtype)
        return 'unknown'
