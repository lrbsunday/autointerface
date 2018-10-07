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


def filter_none(d):
    if isinstance(d, dict):
        delete_keys = []
        for key in d:
            if d[key] is None:
                delete_keys.append(key)
                continue
            filter_none(d[key])
        for key in delete_keys:
            del d[key]
    elif isinstance(d, list):
        for item in d:
            filter_none(item)


def load_config(project_id):
    project = Projects.select().where(Projects.uid == project_id).get()
    project = model_to_dict(project, backrefs=True)

    model_mapping = {model["uid"]: model
                     for model in project["models"]}

    # model_mapping
    project["model_mapping"] = model_mapping

    # model requires
    for model in project["models"]:
        model["requires"] = []
        for field in model["fields"]:
            if field["type"] == "foreign":
                model["requires"].append(
                    model_mapping[field["foreign"]]["name"])

    # 重新组织interface结构
    # interface requires
    interface_group = dict()
    for interface in project["interfaces"]:
        interface_group.setdefault(interface["name"], {
            "requires": [],
            "interfaces": [],
            "name": interface["name"]
        })
        interface_group[interface["name"]]["interfaces"].append(interface)
        for param in interface["params"]:
            if param["field"] is not None and \
                    param["field"]["model"]["name"] != interface["name"]:
                model_name = param["field"]["model"]["name"]
                interface_group[interface["name"]]["requires"].append(
                    model_name)
    project["interfaces"] = list(interface_group.values())

    # 过滤None值
    filter_none(project)

    return project
