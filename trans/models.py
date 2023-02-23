from django.db import models
from common.models import CommonModel
from projects.apis.v1 import project_api

# Create your models here.

class Translation(CommonModel):
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    num = models.IntegerField(null=True)
    remark = models.TextField(null=True, blank=True)
    origin_data = models.TextField()
    trans_data = models.TextField()
    details = models.TextField(null=True)
    is_done = models.BooleanField(default=False)

class CheckTranlation(CommonModel):
    translation = models.ForeignKey("trans.Translation", on_delete=models.CASCADE)
    checker = models.ForeignKey("users.User", on_delete=models.CASCADE)
    note = models.TextField(null=True)
    is_checked = models.BooleanField(default=False)


