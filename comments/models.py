from django.db import models

from projects.models import Project

# Create your models here.
class Comment(models.Model):
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE)
    content = models.CharField(max_length=250)