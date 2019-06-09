# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

#CODE by Gear42
#TODO:加入Redis的写法。

import json
from django.shortcuts import render
from django.views.generic.base import View
from search.models import ImageInfoType
from django.http import HttpResponse
from elasticsearch import Elasticsearch
from datetime import datetime

client = Elasticsearch(hosts=["127.0.0.1:9200"])





class IndexView(View):
    #首页
    def get(self, request):
        #这里的request是一个yield方法。
        #Python的yield
        return render(request, "index.html",) #返回相对应的网站Index网站。

class SearchView(View):
    def get(self, request):
        key_words = request.GET.get("q","")


        s_type = request.GET.get("s_type", "image")

        print(s_type)

        #接收JAVAscript传来的信息。

        page = request.GET.get("p", "1")
        try:
            page = int(page)
        except:
            page = 1

        #翻页需求。

        start_time = datetime.now()
        response = client.search(
            index= "image_tags",
            body={
                "query":{
                    "multi_match":{
                        "query":key_words,
                        "fields":["title"]
                    }
                },
                "from":(page-1)*10,
                "size":10,
                "highlight": {
                    "pre_tags": ['<span class="keyWord">'],
                    "post_tags": ['</span>'],
                    "fields": {
                        "title": {},
                    }
                }
            }
        )

        end_time = datetime.now()

        #统计一个搜索时间。
        last_seconds = (end_time-start_time).total_seconds()


        total_nums = response["hits"]["total"]
        if (page%10) > 0:
            page_nums = int(total_nums/10) +1
        else:
            page_nums = int(total_nums/10)
        hit_list = []

        #搜索结果 and 分页。






        for hit in response["hits"]["hits"]:
            print(hit)
            hit_dict = {} #一个空的字典数组。
            if "title" in hit["highlight"]:
                hit_dict["title"] = "".join(hit["highlight"]["title"])

                #用来表现高光。
            else:
                hit_dict["title"] = hit["_source"]["title"]
            if "content" in hit["highlight"]:
                hit_dict["content"] = "".join(hit["highlight"]["content"])[:500]

            hit_dict["url"] = hit["_source"]["image_url"]
            hit_dict["score"] = hit["_score"]
            hit_list.append(hit_dict)



        print(hit_dict)



        return render(request, "result.html", {"page":page,
                                               "all_hits":hit_list,
                                               "key_words":key_words,
                                               "total_nums":total_nums,
                                               "page_nums":page_nums,
                                               "last_seconds":last_seconds,}
                    )