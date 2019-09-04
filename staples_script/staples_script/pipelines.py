# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
from sqlite3_script import insertScholar, insertOrder, updateOrder
from globals import *
import globals
#from test import order_id

class StaplesScriptPipeline(object):

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = sqlite3.connect("scholars.db", timeout=10)
        self.myCursor = self.connection.cursor()

    def updateOrder(self, item, order_id):
        #NEED TO ADD ITEM_PRICE
        updateSql = """
            UPDATE Orders
            set item_name = ?,
                item_number = ?
            where order_id = ?
            """
        self.myCursor.execute(updateSql, (item['item_name'], item['item_num'], order_id))
        self.connection.commit()


    def process_item(self, item, spider):
        print ("Pipeline Global ID #: ", globals.order_id)
        print ("item received: ", item['item_name'], "\n Item Number: ",item['item_num'])
        self.updateOrder(item, order_id)
        return item
