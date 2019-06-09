# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Text,Keyword,DocType


# 关于数据库模型的代码。
# 主要是ORM架构。
# creator : Gear42

# Create your models here.

connections.create_connection(hosts=["127.0.0.1:9200"]) #创建一个ES连接。

class ImageInfoType(DocType):
    title = Text()
    image_url = Keyword()


if __name__ == "__main__":
    ImageInfoType.init()