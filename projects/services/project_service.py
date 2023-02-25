from rest_framework.exceptions import NotFound
from projects.models import Project

def get_a_project(project_pk) -> Project:
    try:
        project = Project.objects.get(pk=project_pk)
        return project
    except Project.DoesNotExist:
        raise NotFound(detail="Project is not found", code=404)
