from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("projects", projects, name="projects"),
    path("project/<str:id>", single_project, name="single_project"),
]
