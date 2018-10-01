import os
import shutil
from codegen import WORD_DIR
from codegen.render import render


def generate(project_name,
             template_path=WORD_DIR + '/codegen/templates',
             dst_path=WORD_DIR + '/output'):
    config = {
        "project_name": project_name,
        "models": [{
            "name": "orders",
            "requires": ["resources"],
            "rules": [{
                'name': 'name',
                'desc': '订单名称',
                'type': 'string',
                'null': False,
                'unique': True,
                'index': True
            }, {
                'name': 'state',
                'default': 1,
                'type': 'integer',
                'null': False,
                'unique': False,
                'index': False
            }, {
                'name': 'resource',
                'type': 'foreign',
                'model': 'resources',
                'backref': 'orders',
                'on_delete': 'CASCADE'
            }]
        }, {
            "name": "resources",
            "rules": [{
                'name': 'name',
                'desc': '资源名称',
                'type': 'string',
                'null': False,
                'unique': True,
                'index': True
            }, {
                'name': 'state',
                'default': 1,
                'type': 'integer',
                'null': False,
                'unique': False,
                'index': False
            }]
        }],
        "interfaces": [{
            "name": "orders",
            "name_cn": "订单",
            "gets": {
                "params": [{
                    "name": "page",
                    "help_text": "分页页数",
                    "need": False,
                    "default": 1,
                    "type": "integer",
                    "is_filter": False,
                    "is_sorter": False,
                    "is_pager": True,
                }, {
                    "name": "size",
                    "help_text": "分页大小",
                    "need": False,
                    "default": 10,
                    "type": "integer",
                    "is_filter": False,
                    "is_sorter": False,
                    "is_pager": True,
                }, {
                    "name": "name",
                    "help_text": "订单名称",
                    "need": False,
                    "type": "string",
                    "is_filter": True,
                    "is_sorter": False,
                    "is_pager": False,
                }, {
                    "name": "s_name",
                    "model_name": "name",
                    "help_text": "按订单名称排序",
                    "need": False,
                    "type": "string",
                    "choices": ["desc", "asc"],
                    "is_filter": False,
                    "is_sorter": True,
                    "is_pager": False,
                }],
                "recurse": True,
                "backrefs": True
            },
            "get": {
                "recurse": False,
                "backrefs": False
            },
            "post": {
                "params": [{
                    "name": "name",
                    "desc": "订单名称",
                    "need": True,
                    "type": "string"
                }, {
                    "name": "state",
                    "model_name": "state",
                    "help_text": "订单状态",
                    "need": False,
                    "default": 1,
                    "type": "integer",
                }, {
                    "name": "resource_id",
                    "model_name": "resource_id",
                    "help_text": "资源ID",
                    "need": True,
                    "type": "integer",
                }]
            },
            "put": {
                "params": [{
                    "name": "name",
                    "desc": "订单名称",
                    "need": False,
                    "type": "string"
                }, {
                    "name": "state",
                    "model_name": "state",
                    "desc": "订单状态",
                    "need": False,
                    "default": 1,
                    "type": "integer",
                }, {
                    "name": "resource_id",
                    "model_name": "resource_id",
                    "help_text": "资源ID",
                    "need": False,
                    "type": "integer",
                }]
            },
            "delete": {

            }
        }, {
            "name": "resources",
            "name_cn": "资源",
            "gets": {
                "params": [{
                    "name": "page",
                    "help_text": "分页页数",
                    "need": False,
                    "default": 1,
                    "type": "integer",
                    "is_filter": False,
                    "is_sorter": False,
                    "is_pager": True,
                }, {
                    "name": "size",
                    "help_text": "分页大小",
                    "need": False,
                    "default": 10,
                    "type": "integer",
                    "is_filter": False,
                    "is_sorter": False,
                    "is_pager": True,
                }, {
                    "name": "name",
                    "help_text": "资源名称",
                    "need": False,
                    "type": "string",
                    "is_filter": True,
                    "is_sorter": False,
                    "is_pager": False,
                }, {
                    "name": "s_name",
                    "model_name": "name",
                    "help_text": "按订单名称排序",
                    "need": False,
                    "type": "string",
                    "choices": ["desc", "asc"],
                    "is_filter": False,
                    "is_sorter": True,
                }],
                "recurse": True,
                "backrefs": True
            },
            "get": {
                "recurse": False,
                "backrefs": False
            },
            "post": {
                "params": [{
                    "name": "name",
                    "desc": "资源名称",
                    "need": True,
                    "type": "string"
                }, {
                    "name": "state",
                    "model_name": "state",
                    "help_text": "资源状态",
                    "need": False,
                    "default": 1,
                    "type": "integer",
                }]
            },
            "put": {
                "params": [{
                    "name": "name",
                    "desc": "资源名称",
                    "need": False,
                    "type": "string"
                }, {
                    "name": "state",
                    "model_name": "state",
                    "desc": "资源状态",
                    "need": False,
                    "default": 1,
                    "type": "integer",
                }]
            },
            "delete": {}
        }]
    }

    template_path = template_path.rstrip('/')
    dst_path = dst_path.rstrip('/')

    if dst_path != WORD_DIR:
        shutil.rmtree(dst_path, ignore_errors=True)

    for root, dirs, files in os.walk(template_path):
        relative_path = root[len(template_path) + 1:]
        for src_filename in files:
            dst_filename = os.path.splitext(src_filename)[0]
            source = os.path.join(relative_path, src_filename)
            if '{{' in dst_filename:
                continue

            destination = os.path.join(dst_path, relative_path,
                                       dst_filename)
            destination = destination.replace('{{ project_name }}',
                                              project_name)
            context = config
            render(source, destination, **context)

    model_template_filename = \
        "{{ project_name }}/models/{{ model_name }}.py.html"
    for model in config["models"]:
        destination = os.path.join(dst_path,
                                   model_template_filename
                                   .replace('{{ project_name }}',
                                            project_name)
                                   .replace('{{ model_name }}',
                                            model['name'])[:-5])
        context = {
            "project_name": project_name
        }
        context.update(model)
        render(model_template_filename, destination, **context)

    interface_template_filename = \
        "{{ project_name }}/web/{{ interface_name }}.py.html"
    for interface in config["interfaces"]:
        destination = os.path.join(dst_path,
                                   interface_template_filename
                                   .replace('{{ project_name }}',
                                            project_name)
                                   .replace('{{ interface_name }}',
                                            interface['name'])[:-5])
        context = {
            "project_name": project_name
        }
        context.update(interface)
        render(interface_template_filename, destination, **context)


generate('test')
