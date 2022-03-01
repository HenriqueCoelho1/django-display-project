from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("project", project, name="project"),
    path("projects/<int:id>", project_id, name="project_id"),
]
