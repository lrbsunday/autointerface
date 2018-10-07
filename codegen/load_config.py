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

    model_mapping = {model["uid"]: model
                     for model in project["models"]}
    project["model_mapping"] = model_mapping
    for model in project["models"]:
        model["requires"] = []
        for field in model["fields"]:
            if field["type"] == "foreign":
                model["requires"].append(
                    model_mapping[field["foreign"]]["name"])

    interface_group = dict()
    for interface in project["interfaces"]:
        interface_group.setdefault(interface["name"], {
            "requires": [],
            "interfaces": [],
            "name": interface["name"]
        })
        interface_group[interface["name"]]["interfaces"].append(interface)
    project["interfaces"] = list(interface_group.values())

    return project
