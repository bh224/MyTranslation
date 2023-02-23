from django.urls import path
from projects.apis.v1 import project_api
from comments.apis.v1 import comment_api
from . import views

urlpatterns = [
    path("", project_api.Projects.as_view()),
    path("<int:pk>/comments", comment_api.Comments.as_view()),
]
