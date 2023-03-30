from django.urls import path
from glossaries.apis.v1 import glossary_api
from . import views

urlpatterns = [
    path("scrap-names", glossary_api.ScrapNames.as_view()),
    path("recommend-names", glossary_api.RandomNames.as_view()),
]
