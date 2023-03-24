from django.urls import path
from . import views
from users.apis.v1 import user_api


urlpatterns = [
    path("", user_api.Users.as_view()),
    path("me", user_api.UserDetail.as_view()),
    path("logout", user_api.LogOut.as_view()),
]
