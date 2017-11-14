# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

from final.items import FinalItem
#肝啊！
class FinalspiderSpider(scrapy.Spider):
    name = 'finalspider'
    allowed_domains = ['www.58pic.com']
    start_urls = ['http://www.58pic.com/piccate/9-187-820-1.html']
    def parse_detail(self,response):
        final_item = FinalItem()
        #具体爬取每一个图片的标题与url并且保存在items里面
        # print(response.url)
        # css_text = ".detail-title>h1:nth-child(1)>p:nth-child(1)::text"
        # text = response.css(css_text).extract()
        # print(text)
        css_img_url = "#show-area-pic::attr(src)"
        img_url = response.css(css_img_url).extract()[0][0:-8]
        print(img_url)
        final_item["image_url"] =img_url
        final_item["title"] = "TEST"

    def parse_html(self,response):
        css_head = "div.flow-item:nth-child("
        css_end = ") > div:nth-child(1) > a:nth-child(1)::attr(href)"
        for i in range(5):#更改每个页面的数据
            css_combine = css_head + (str)(i+1) + css_end
            url = response.css(css_combine).extract()[0]
            # css_text = 'div.flow-item:nth-child(1)>div:nth-child(1)>a:nth-child(3)::text'
            # txt = response.css(css_text).extract()[0]
            #print(txt)
            yield Request(url,callback=self.parse_detail)
    def parse(self, response):
        #分析当前页的所有图片链接并且翻到下一页
        root_url = "http://www.58pic.com/piccate/9-187-820-"
        url_all_pages = []
        for i in range(5):
            url = root_url+(str)(i+1)+".html"
            url_all_pages.append(url)
        #获取所有页面的url
        for url_page in url_all_pages:
            yield Request(url_page,callback=self.parse_html)
        # css1 = "div.flow-item:nth-child(2) > div:nth-child(1) > a:nth-child(1)::attr(href)"
        # url = response.css(css1).extract()[0]
        # print(url)
        # yield Request(url=url_all_pages[3],callback=self.parse)
        # print(response.url)
        # css1 = "div.flow-item:nth-child(2) > div:nth-child(1) > a:nth-child(1)::attr(href)"
        # url = response.css(css1).extract()[0]
        # print(url)
        # #css规则获取
        # #Request(url=url_all_pages[3])
        #
        # #具体图片css规则：
        # img_css = "#show-area-pic::attr(src)"#需要去除后缀
        #
        #
        # #保存到items


