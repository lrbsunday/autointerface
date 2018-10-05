from playhouse.shortcuts import model_to_dict
from autointerface.models.projects import Projects
# 为了要得到递归结果，下面的模块即使不用也不能注释掉
# noinspection PyUnresolvedReferences
from autointerface.models.models import Models
# noinspection PyUnresolvedReferences
from autointerface.models.fields import Fields
# noinspection PyUnresolvedReferences
from autointerface.models.interfaces import Interfaces
# noinspection PyUnresolvedReferences
from autointerface.models.params import Params


def load_config(project_id):
    project = Projects.select().where(Projects.uid == project_id).get()
    project = model_to_dict(project, backrefs=True, recurse=True)

    project["model_mapping"] = {model["uid"]: model
                                for model in project["models"]}
    return project
