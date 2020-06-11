# -*- coding: utf-8 -*-

from hashtag.models import ScrapyItem
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class HashtagImagesPipeline:

    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'),
            


             # this will be passed from django view
        )

    def close_spider(self, spider):
        # And here we are saving our crawled data with django models.
        # item = ScrapyItem()
        # item.unique_id = self.unique_id
        # item.data =
        # item.save()
        # return item
        print("SPIDER CLOSED")

    def process_item(self, item, spider):
        scrapy_item = ScrapyItem()
        scrapy_item.unique_id = self.unique_id
        scrapy_item.data = item.get('data')
        scrapy_item.save()
        return item