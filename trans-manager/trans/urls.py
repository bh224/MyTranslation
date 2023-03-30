from django.urls import path
from . import views
from trans.apis.v1 import translation_api

urlpatterns = [
    path("papago", translation_api.PapagoAPI.as_view()),
]
