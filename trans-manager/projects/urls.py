from django.urls import path
from projects.apis.v1 import project_api
from comments.apis.v1 import comment_api
from glossaries.apis.v1 import category_api, glossary_api
from trans.apis.v1 import translation_api
from . import views

urlpatterns = [
    path("", project_api.Projects.as_view()),
    path("test", project_api.Tests.as_view()),
    path("<int:pk>", project_api.ProjectDetail.as_view()),
    path("<int:pk>/send-email", project_api.SendEmail.as_view()),
    path("<int:pk>/comments", comment_api.Comments.as_view()),
    path("<int:pk>/categories", category_api.Categories.as_view()),
    path("<int:pk>/glossaries", glossary_api.Glossaries.as_view()),
    path("<int:pk>/glossaries/marker", glossary_api.Marker.as_view()),
    path("<int:pk>/translations", translation_api.Translations.as_view()),
    path("<int:pk>/checks", translation_api.Check.as_view()),
    path("upload/project", project_api.ProjectMembers.as_view()),

]
