from django.db import models
from common.models import CommonModel

# Create your models here.
class Glossary(CommonModel):
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    category = models.CharField(max_length=120)
    original = models.CharField(max_length=250)
    translation = models.CharField(max_length=250)
    details = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)

