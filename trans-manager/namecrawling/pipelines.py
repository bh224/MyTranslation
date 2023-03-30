# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from glossaries.models import NameRecommend
from asgiref.sync import sync_to_async


class NamecrawlingPipeline:
    @sync_to_async
    def process_item(self, item, spider):
        name = NameRecommend()
        name.last_name = item['last_name']
        name.first_name = item['first_name']
        name.furigana = item['furigana']
        name.sex = item['sex']
        name.save()
        return item