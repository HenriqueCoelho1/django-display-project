from django.shortcuts import redirect, render
from core.models import Project
from .forms import ProjectForm


def index(request):
    template_name = "projects/index.html"
    return render(request, template_name)


def projects(request):
    content = {}
    template_name = "projects/projects.html"
    projects = Project.objects.all()
    content.update({"projects": projects})
    return render(request, template_name, content)


def single_project(request, id):
    content = {}
    template_name = "projects/single_project.html"
    project = Project.objects.get(id=id)
    content.update({"project": project})
    tags = project.tags.all()
    content.update({"tags": tags})

    return render(request, template_name, {"project": project})


def create_project(request):
    template_name = "projects/project_form.html"
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("projects")
    content = {"form": form}
    return render(request, template_name, content)


def update_project(request, id):
    template_name = "projects/project_form.html"
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")
    content = {"form": form}
    return render(request, template_name, content)


def delete_project(request, id):
    template_name = "projects/delete_template.html"
    project = Project.objects.get(id=id)
    if request.method == "POST":
        project.delete()
        return redirect("projects")
    context = {"object": project}
    return render(request, template_name, context)
