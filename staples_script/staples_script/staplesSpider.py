from staples_script.items import StaplesScriptItem
import scrapy
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class StaplesSpider(scrapy.Spider):
    name = 'staples'
    #start_urls = []
    start_urls = ['https://www.staplesadvantage.com/shop/StplShowItem?rdrKeyword=24377015&singlepage=true&icid=&catalogId=4&item_id=197192262&langId=-1&currentSKUNbr=24377015&storeId=10101&itemType=1',
    'https://www.staplesadvantage.com/shop/StplShowItem?catalogId=4&item_id=189237920&langId=-1&currentSKUNbr=24377312&storeId=10101&itemType=1&staplesChoice=1&addWE1ToCart=true&documentID=dd4d20df3be5c7ed2d4036982c291bfdd21cc075']

    def parse (self, response):
        #to get the item number
        for label in response.xpath("//span[@class='search-prod-num adafont']"):
            loader = ItemLoader(item=StaplesScriptItem(),selector=label)
            loader.add_xpath('item_num', "//span[@class='search-prod-num adafont']/span")
        #to get the item name
        loader.add_xpath('item_name', "//h1[@class='search-prod-desc disp-block font-norm']")
        #to get the item price
        #loader.add_xpath('item_price')""",putPricePath when you have log in information)"""
        yield loader.load_item()
