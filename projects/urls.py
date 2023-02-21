from django.urls import path
from projects.apis.v1 import project_api
from . import views

urlpatterns = [
    path("", project_api.Projects.as_view()),
]
