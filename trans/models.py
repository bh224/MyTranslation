from django.db import models
from common.models import CommonModel

# Create your models here.

class Translation(CommonModel):
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    num = models.IntegerField(null=True)
    remark = models.TextField(null=True, blank=True)
    origin_data = models.TextField()
    trans_data = models.TextField()
    note = models.TextField(null=True)
    is_checked = models.BooleanField(null=False)
    is_done = models.BooleanField(default=False)

