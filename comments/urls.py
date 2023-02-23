from django.urls import path
from . import views
from comments.apis.v1 import comment_api

urlpatterns = [
    path("<int:pk>", comment_api.CommentDetail.as_view()),
]
