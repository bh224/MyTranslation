from django.urls import path
from projects.apis.v1 import project_api
from comments.apis.v1 import comment_api
from glossaries.apis.v1 import category_api, glossary_api
from trans.apis.v1 import translation_api
from . import views

urlpatterns = [
    path("", project_api.Projects.as_view()),
    path("<int:pk>/comments", comment_api.Comments.as_view()),
    path("<int:pk>/categories", category_api.Category.as_view()),
    path("<int:pk>/glossaries", glossary_api.Glossary.as_view()),
    path("<int:pk>/translations", translation_api.Translations.as_view()),
    path("<int:pk>/checks", translation_api.Check.as_view()),

]
