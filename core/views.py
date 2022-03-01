from django.shortcuts import render


def index(request):
    template_name = "projects/index.html"
    return render(request, template_name)


def project(request):
    template_name = "projects/project.html"
    return render(request, template_name)


def project_id(request, id):
    template_name = "projects/project_id.html"
    return render(request, template_name)
