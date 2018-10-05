import logging


def format_value(value):
    if value is None:
        return 'None'
    elif isinstance(value, int):
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
    elif vtype == 'list':
        return 'list'
    else:
        logging.error("不支持的接口参数类型%s" % vtype)
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
    elif vtype == 'json':
        return 'JSONField'
    elif vtype == 'foreign':
        return 'ForeignKeyField'
    else:
        logging.error("不支持的模型字段类型%s" % vtype)
        return 'unknown'


def get_model_field(rule, name):
    model_field = rule.get('model_field') or rule.get('name', '')
    if '.' in model_field:
        return model_field
    else:
        return name + '.' + model_field


def split(value, split_char):
    return value.split(split_char)


def index(value, i):
    return value[i]
