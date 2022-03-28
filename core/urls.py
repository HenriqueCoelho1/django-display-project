from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("projects/", projects, name="projects"),
    path("project/<str:id>/", single_project, name="single_project"),
    path("create-project/", create_project, name="create_project"),
    path("update-project/<str:id>/", update_project, name="update_project"),
    path("delete-project/<str:id>/", delete_project, name="delete_project"),
]
