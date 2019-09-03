# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
import re
import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def remove_words(string_value):
    #after we have it into a string, we can finally manipulate it, so in this case we remove everything that isn't letters or numbers
    newString = re.sub("[^\w]", "", string_value)
    #now that we have just letters and numbers, we remove the numbers to get the item number
    number =  re.sub("\D","", newString)
    #print(type(number), number)
    return (number)

def remove_symbols(string_value):
    #this gets rid of spaces, and other characters that aren't letters or numbers and subtitutes them with a space
    newString = re.sub("[^\w]", " ", string_value)
    #this getse rid of duplicate whitespaces
    finalString = re.sub(r'\s+', ' ', newString)
    return (finalString)

def remove_second_half(string_data):
    first_half = string_data.split('(')
    #print ("THIS IS THE SHIT: ",type(first_half), first_half)
    return (first_half)



class StaplesScriptItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    item_num = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_words),
        output_processor = TakeFirst()
    )
    item_name = scrapy.Field(
        input_processor = MapCompose(remove_tags, remove_symbols, remove_second_half),
        output_processor = TakeFirst()
        )
    item_price = scrapy.Field()
