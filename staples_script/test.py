
import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
import globals

test_urls = ['https://www.staplesadvantage.com/shop/StplShowItem?rdrKeyword=24377015&singlepage=true&icid=&catalogId=4&item_id=197192262&langId=-1&currentSKUNbr=24377015&storeId=10101&itemType=1']

next_url = 'https://www.staplesadvantage.com/shop/StplShowItem?catalogId=4&item_id=189237920&langId=-1&currentSKUNbr=24377312&storeId=10101&itemType=1&staplesChoice=1&addWE1ToCart=true&documentID=dd4d20df3be5c7ed2d4036982c291bfdd21cc075'
counter = 0


process = CrawlerProcess(get_project_settings())
while counter < 3:
    if counter == 0:
        globals.order_id = 1
        process.crawl("staples", start_urls = test_urls)
        test_urls.pop(0)
        test_urls.append(next_url)

    if counter == 1:
        globals.order_id = 2
        #process.crawl("staples")
    print("Iteration #: ",counter)
    counter += 1

process.start()





"""
 # the script will block here until the crawling is finished
import globals

def printId():
    print (globals.order_id)
"""
