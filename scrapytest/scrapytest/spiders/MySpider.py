import scrapy
import urllib
import os
from scrapy.http import Request
from scrapytest.CourseItems import CourseItem
class MySpider(scrapy.Spider):
    name = "MySpider";
    allowed_domains = ["cssmoban.com"];
    start_urls = ["http://www.cssmoban.com/tags.asp?page=2&n=Bootstrap"]
    def parse(self, response):
        item = CourseItem();
        list = response.xpath('//ul[@class="thumbItem large clearfix"]//li//img')
        # print(list)
        for box in list:
            a=3
            # filename = response.url.split("/")[-2]
            # with open(filename, 'wb') as f:
            #     f.write(response.body)
            # 获取每个div中的课程路径
            src= "http://www.cssmoban.com"+box.xpath('./@src').extract()[0]
            item['url'] = src
            print(src)
            if src:
                absoluteSrc = src
                file_name = src.split("/")[-1]
                file_path = os.path.join("F:\\pics", file_name)
                urllib.request.urlretrieve(absoluteSrc, file_path)

        nexturl = "http://www.cssmoban.com/tags.asp"+box.xpath('//a[@class="num"]/@href').extract()[0]
        print(nexturl)
        yield Request(nexturl, callback=self.parse)