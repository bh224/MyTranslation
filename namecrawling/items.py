from scrapy_djangoitem import DjangoItem
from glossaries.models import NameRecommend

# class NamecrawlingItem(DjangoItem):
    # django_model = NameRecommend

from scrapy.item import Item, Field

class NamecrawlingItem(Item):
    pass