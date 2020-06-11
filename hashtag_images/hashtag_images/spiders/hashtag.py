# -*- coding: utf-8 -*-
import scrapy, time
from scrapy_selenium import SeleniumRequest
from django.utils import timezone
from scrapy import Selector
from .. import items
from shutil import which
from .. import settings as check_settings
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# SELENIUM_DRIVER_NAME = 'chrome',
# SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver'),
# SELENIUM_DRIVER_ARGUMENTS = ['-headless']

class HashtagSpider(scrapy.Spider):
    name = 'new_hashtag'

    def __init__(self, *args, **kwargs):
        self.allowed_domains = ['twitter.com']
        self.unique_id = kwargs.get('unique_id')


    start_urls = ['https://twitter.com/']
    SCROLL_PAUSE_TIME = 2

    # def start_requests(self):
    #     # yield SeleniumRequest(url="https://twitter.com/hashtag/blacklivesmatter", wait_time=3, screenshot=True, callback=self.parse)
    #     yield SeleniumRequest(url="https://twitter.com/hashtag/{}".format(self.unique_id), wait_time=10, screenshot=True,
    #                           callback=self.parse)

    def parse(self, response):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
        driver.get("https://twitter.com/hashtag/{}".format(self.unique_id)) 

        print(check_settings.SELENIUM_DRIVER_NAME)
        print(check_settings.SELENIUM_DRIVER_EXECUTABLE_PATH)

        # driver = response.meta['driver']

        driver.find_element_by_xpath("(//div[@role='presentation'])[position() > 5]").click()
        time.sleep(1)
        last_height = driver.execute_script("return document.body.scrollHeight")

        for i in range(1, 11):
            html = driver.page_source
            response_obj = Selector(text=html)
            for link in response_obj.xpath("//img[contains(@src, 'https://pbs.twimg.com/media/')]"):
                # yield {
                #     'img_url': link.xpath(".//@src").get()
                # }
                item = items.HashtagImagesItem()
                item['unique_id'] = self.unique_id
                item['data'] = link.xpath(".//@src").get()
                yield item

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # driver.save_screenshot('pageprevious{}.png'.format(i))

            # driver.find_element_by_class_name("result--more__btn btn btn--full").click()
            # driver.find_element_by_xpath("//a[@class='result--more__btn btn btn--full']").click()

            # Wait to load page
            time.sleep(self.SCROLL_PAUSE_TIME)
            # driver.save_screenshot('pageafter{}.png'.format(i))

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height


