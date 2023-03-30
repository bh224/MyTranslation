import os
import time, random
from celery import shared_task



@shared_task
def scrap_names(sex):
    # os.system("scrapy crawl names")
    # os.system(f"scrapy crawl names -O randomname.json -a country={country} -a sex={sex}")
    os.system(f"scrapy crawl names -a sex={sex}")
    return "done"