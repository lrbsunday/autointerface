from codegen.codegen import generate

config = {
    "project_name": "test",
    "models": [{
        "name": "orders",
        "requires": ["resources"],
        "rules": [{
            'name': 'name',
            'description': '订单名称',
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
            'description': '资源名称',
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
        "requires": ["resources"],
        "gets": {
            "params": [{
                "name": "page",
                "description": "分页页数",
                "need": False,
                "default": 1,
                "min": 1,
                "max": 3,
                "vtype": "integer",
                "is_filter": False,
                "is_sorter": False,
                "is_pager": True,
            }, {
                "name": "size",
                "description": "分页大小",
                "need": False,
                "default": 10,
                "vtype": "integer",
                "is_filter": False,
                "is_sorter": False,
                "is_pager": True,
            }, {
                "name": "name",
                "description": "订单名称",
                "need": False,
                "vtype": "string",
                "is_filter": True,
                "is_sorter": False,
                "is_pager": False,
                "filter_op": "%"
            }, {
                "name": "s_name",
                "model_field": "name",
                "description": "按订单名称排序",
                "need": False,
                "vtype": "string",
                "choices": ["desc", "asc"],
                "is_filter": False,
                "is_sorter": True,
                "is_pager": False,
            }, {
                "name": "resource_name",
                "model_field": "Resources.name",
                "description": "按资源名称过滤",
                "need": False,
                "vtype": "string",
                "is_filter": True,
                "is_sorter": False,
                "is_pager": False,
                "filter_condition": "Resources.name.startswith(resource_name)"
            }, {
                "name": "s_resource_name",
                "model_field": "Resources.name",
                "description": "按资源名称排序",
                "need": False,
                "vtype": "string",
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
                "vtype": "string"
            }, {
                "name": "state",
                "model_field": "state",
                "description": "订单状态",
                "need": False,
                "default": 1,
                "vtype": "integer",
            }, {
                "name": "resource_id",
                "model_field": "resource_id",
                "description": "资源ID",
                "need": True,
                "vtype": "integer",
            }]
        },
        "put": {
            "params": [{
                "name": "name",
                "desc": "订单名称",
                "need": False,
                "vtype": "string"
            }, {
                "name": "state",
                "model_field": "state",
                "desc": "订单状态",
                "need": False,
                "default": 1,
                "vtype": "integer",
            }, {
                "name": "resource_id",
                "model_field": "resource_id",
                "description": "资源ID",
                "need": False,
                "vtype": "integer",
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
                "description": "分页页数",
                "need": False,
                "default": 1,
                "vtype": "integer",
                "is_filter": False,
                "is_sorter": False,
                "is_pager": True,
            }, {
                "name": "size",
                "description": "分页大小",
                "need": False,
                "default": 10,
                "vtype": "integer",
                "is_filter": False,
                "is_sorter": False,
                "is_pager": True,
            }, {
                "name": "name",
                "description": "资源名称",
                "need": False,
                "vtype": "string",
                "is_filter": True,
                "is_sorter": False,
                "is_pager": False,
            }, {
                "name": "s_name",
                "model_field": "name",
                "description": "按订单名称排序",
                "need": False,
                "vtype": "string",
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
                "vtype": "string"
            }, {
                "name": "state",
                "model_field": "state",
                "description": "资源状态",
                "need": False,
                "default": 1,
                "vtype": "integer",
            }]
        },
        "put": {
            "params": [{
                "name": "name",
                "desc": "资源名称",
                "need": False,
                "vtype": "string"
            }, {
                "name": "state",
                "model_field": "state",
                "desc": "资源状态",
                "need": False,
                "default": 1,
                "vtype": "integer",
            }]
        },
        "delete": {}
    }]
}

generate(config)
