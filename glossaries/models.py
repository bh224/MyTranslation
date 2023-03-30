from django.db import models
from common.models import CommonModel

# Create your models here.
class Glossary(CommonModel):
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    category = models.ForeignKey("glossaries.Category", on_delete=models.CASCADE)
    origin_word = models.CharField(max_length=250)
    furigana = models.CharField(max_length=250, null=True, blank=True)
    trans_word = models.CharField(max_length=250)
    details = models.TextField(null=True, blank=True)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)

class Category(CommonModel):
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=120)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)

    
class NameRecommend(CommonModel):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    furigana = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
