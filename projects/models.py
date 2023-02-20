from django.db import models
from common.models import CommonModel

# Create your models here.
class Rawdata(CommonModel):
    projects = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    row = models.CharField(max_length=250)
    is_use = models.BooleanField(default=True)
    sheets = models.CharField(max_length=120)

class Project(CommonModel):
    category = models.CharField(max_length=120)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    members = models.ManyToManyField("users.User", through="Project_Member", related_name="projects")
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)

class Project_Member(CommonModel):
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    member = models.ForeignKey("users.User", on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
