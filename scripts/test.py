from codegen.render import render
from codegen import WORD_DIR

render('model.html', WORD_DIR + '/output/model.py',
       name='orders',
       rules=[{
           'name': 'name',
           'desc': '哈哈哈',
           'default': 'name',
           'type': 'string',
           'null': True,
           'unique': True,
           'index': True
       }, {
           'name': 'state',
           'default': 1,
           'type': 'float',
           'null': False,
           'unique': False,
           'index': False
       }])

render('interface.html', WORD_DIR + '/output/interface.py',
       name='orders',
       name_cn="订单",
       gets={
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
               "model_field": "name",
               "help_text": "按订单名称排序",
               "need": False,
               "type": "string",
               "choices": ["desc", "asc"],
               "is_filter": False,
               "is_sorter": True,
               "is_pager": False,
           }]
       },
       get={

       },
       post={
           "params": [{
               "name": "name",
               "desc": "订单名称",
               "need": True,
               "type": "string"
           }, {
               "name": "state",
               "model_field": "state",
               "help_text": "订单状态",
               "need": False,
               "default": 1,
               "type": "integer",
           }]
       },
       put={
           "params": [{
               "name": "name",
               "desc": "订单名称",
               "need": True,
               "type": "string"
           }, {
               "name": "state",
               "model_field": "state",
               "desc": "订单状态",
               "need": False,
               "default": 1,
               "type": "integer",
           }]
       },
       delete={

       }
       )
