# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from models.es_types import Image
class FinalItem(scrapy.Item):#
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_url = scrapy.Field()
    title = scrapy.Field()
    # def sava_to_es(self,):
    #     image= Image()
    #     image.img_url = self["image_url"]
    #     image.title = self["title"]

