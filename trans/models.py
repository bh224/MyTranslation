from django.db import models
from common.models import CommonModel
from projects.apis.v1 import project_api

# Create your models here.

class Translation(CommonModel):
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    num = models.IntegerField()
    remark = models.TextField(null=True, blank=True)
    origin_data = models.TextField()
    trans_data = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

class CheckTranslation(CommonModel):
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    translation = models.ForeignKey("trans.Translation", null=True, blank=True, on_delete=models.CASCADE, related_name="translations")
    checker = models.ForeignKey("users.User", on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True)
    is_checked = models.BooleanField(default=False)


