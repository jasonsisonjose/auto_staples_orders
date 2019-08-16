# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import unicodedata
import re
import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def remove_words(unicode_value):
    #currently the extracted data is in unicode, so we make it into a string
    string_value = unicode_value.encode('ascii','ignore')
    #after we have it into a string, we can finally manipulate it, so in this case we remove everything that isn't letters or numbers
    newString = re.sub("[^\w]", "", string_value)
    #now that we have just letters and numbers, we remove the numbers to get the item number
    number =  re.sub("\D","", newString)
    return (number)

def remove_symbols(unicode_value):
    #currently the extracted data is in unicode, so we make it into a string
    string_value = unicode_value.encode('ascii','ignore')
    return (string_value)

def remove_second_half(string_data):
    first_half = string_data.split('(')
    return (first_half)


class StaplesScriptItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    item_num = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_words),
        output_processor = TakeFirst()
    )
    item_name = scrapy.Field(
        input_processor = MapCompose(remove_tags,remove_symbols, remove_second_half),
        output_processor = TakeFirst()
        )
    item_price = scrapy.Field()
