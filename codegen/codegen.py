import os
import shutil

from codegen.render import render
from codegen import WORD_DIR


def generate(project,
             template_path=WORD_DIR + "/codegen/templates",
             dst_path=WORD_DIR + "/output"):
    project_name = project["name"]
    template_path = template_path.rstrip("/")
    dst_path = dst_path.rstrip("/")

    if dst_path != WORD_DIR:
        shutil.rmtree(dst_path, ignore_errors=True)

    for root, dirs, files in os.walk(template_path):
        relative_path = root[len(template_path) + 1:]
        for src_filename in files:
            dst_filename = os.path.splitext(src_filename)[0]
            source = os.path.join(relative_path, src_filename)
            if "{{" in dst_filename:
                continue

            destination = os.path.join(dst_path, relative_path,
                                       dst_filename)
            destination = destination.replace("{{ project_name }}",
                                              project_name)
            context = {
                "project": project
            }
            render(source, destination, **context)

    model_template_filename = \
        "{{ project_name }}/models/{{ model_name }}.py.html"
    for model in project["models"]:
        destination = os.path.join(dst_path,
                                   model_template_filename
                                   .replace("{{ project_name }}",
                                            project_name)
                                   .replace("{{ model_name }}",
                                            model["name"])[:-5])
        context = {
            "project": project,
            "model": model
        }
        render(model_template_filename, destination, **context)

    interface_template_filename = \
        "{{ project_name }}/web/{{ interface_name }}.py.html"
    for interface in project["interfaces"]:
        destination = os.path.join(dst_path,
                                   interface_template_filename
                                   .replace("{{ project_name }}",
                                            project_name)
                                   .replace("{{ interface_name }}",
                                            interface["name"])[:-5])
        context = {
            "project": project,
            "interfaces": interface
        }
        render(interface_template_filename, destination, **context)
