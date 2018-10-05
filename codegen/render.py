import os

from jinja2 import Environment, PackageLoader, select_autoescape
import autopep8

from codegen.filters import *

env = Environment(
    loader=PackageLoader('codegen', 'templates'),
    autoescape=select_autoescape([]),
    extensions=['jinja2.ext.do', 'jinja2.ext.loopcontrols'],
    trim_blocks=True,
    lstrip_blocks=True
)
env.filters['format_value'] = format_value
env.filters['format_param_type'] = format_param_type
env.filters['format_model_type'] = format_model_type
env.filters['get_model_field'] = get_model_field
env.filters['split'] = split
env.filters['index'] = index


def render(source, destination, **context):
    path = os.path.dirname(destination)
    if not os.path.exists(path):
        os.makedirs(path)

    template = env.get_template(source)
    code = template.render(**context)
    code = autopep8.fix_code(code,
                             options={'aggressive': 0,
                                      'max_line_length': 79})
    with open(destination, "w", encoding="utf-8") as fp:
        fp.write(code)
