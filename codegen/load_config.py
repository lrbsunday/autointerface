import json
from playhouse.shortcuts import model_to_dict

from autointerface.models.projects import Projects
from autointerface.common.tools import DefaultEncoder
# 为了要得到递归结果，下面的模块即使不用也不能注释掉
from autointerface.models.models import Models
from autointerface.models.fields import Fields
from autointerface.models.interfaces import Interfaces
from autointerface.models.params import Params


def load_config():
    project = Projects.select().where(Projects.uid == 1).get()
    project = model_to_dict(project, backrefs=True, recurse=True)
    print(json.dumps(project, cls=DefaultEncoder))


load_config()
