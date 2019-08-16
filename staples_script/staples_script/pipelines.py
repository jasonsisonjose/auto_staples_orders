# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3



class StaplesScriptPipeline(object):

    def __init__ (self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.myConnection = sqlite3.connect("scholars.db")
        self.myCursor = self.myConnection.cursor()

    def create_table(self):
        dropCommand = """DROP TABLE IF EXISTS Scholars"""
        self.myCursor.execute(dropCommand)
        self.myConnection.commit()

        scholars_sql = """
        CREATE TABLE Scholars
            (
            cwid integer PRIMARY KEY,
            first_name varchar(20) NOT NULL,
            last_name varchar(20) NOT NULL,
            acct_balance real NOT NULL,
            cohort varchar(20) NOT NULL
            )
            """

        self.myCursor.execute(scholars_sql)
        self.myConnection.commit()

        dropCommand = """DROP TABLE IF EXISTS Orders"""
        self.myCursor.execute(dropCommand)
        self.myConnection.commit()
        orders_sql = """
        CREATE TABLE Orders
            (
            cwid integer PRIMARY KEY,
            item_number integer NOT NULL,
            item_name varchar(20) NOT NULL,
            item_price real NOT NULL,
            item_quantity integer NOT NULL
            )
            """
        self.myCursor.execute(orders_sql)
        self.myConnection.commit()

        dropCommand = """DROP TABLE IF EXISTS Products"""
        self.myCursor.execute(dropCommand)
        self.myConnection.commit()
        products_sql = """
        CREATE TABLE Products
            (
            item_number integer NOT NULL,
            item_name varchar(20) NOT NULL,
            )
            """
        #self.myCursor.execute(products_sql)
        #self.myConnection.commit()

    def process_item(self, item, spider):
        self.insert_into_db(item)
        return item


    def insert_into_db(self, item):
        insertCommand = """INSERT INTO Orders VALUES (?,?)"""(
            item['item_num'], item['item_name']
        )
        self.myCursor.execute(insertCommand)
        self.myConnection.commit()
