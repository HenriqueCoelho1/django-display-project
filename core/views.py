from django.shortcuts import render

from core.models import Project


def index(request):
    template_name = "projects/index.html"
    return render(request, template_name)


def projects(request):
    context = {}
    template_name = "projects/projects.html"
    projects = Project.objects.all()
    context.update({"projects": projects})
    return render(request, template_name, context)


def single_project(request, id):
    context = {}
    template_name = "projects/single_project.html"
    project = Project.objects.get(id=id)
    context.update({"project": project})
    tags = project.tags.all()
    context.update({"tags": tags})

    return render(request, template_name, {"project": project})
