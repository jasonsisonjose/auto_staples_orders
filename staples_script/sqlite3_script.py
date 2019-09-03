import sqlite3
from globals import Scholar, Order
import globals

def create_table():
    connection = sqlite3.connect("scholars.db", timeout=10)
    myCursor = connection.cursor()
    scholars_sql = """
    CREATE TABLE IF NOT EXISTS Scholars
        (
        cwid integer PRIMARY KEY,
        first_name varchar(20) ,
        last_name varchar(20),
        acct_balance real DEFAULT 100.00,
        cohort varchar(20)
        )
        """
    myCursor.execute(scholars_sql)
    connection.commit()

    orders_sql = """
    CREATE TABLE IF NOT EXISTS Orders
        (
        order_id integer PRIMARY KEY AUTOINCREMENT,
        cwid integer,
        item_number integer ,
        item_name varchar(20) ,
        item_price real ,
        item_quantity integer
        )
        """
    myCursor.execute(orders_sql)
    connection.commit()

def insertScholar(tempScholar):
    create_table()
    connection = sqlite3.connect("scholars.db", timeout=10)
    myCursor = connection.cursor()
    insertSql = """
        INSERT INTO Scholars (cwid, first_name,last_name,cohort) VALUES (?,?,?,?)
        """
    #use try and except block to let code flow, in case the cwid is the same
    try:
        myCursor.execute(insertSql, (tempScholar.cwid, tempScholar.first_name, tempScholar.last_name, tempScholar.cohort))
        connection.commit()
    except:
    #this tries to update Scholars table if they are the same CWID
        updateSql = """
            UPDATE Scholars
            SET first_name = ?,
                last_name = ?,
                cohort = ?
            WHERE cwid = ?
            """
        myCursor.execute(updateSql, (tempScholar.first_name, tempScholar.last_name, tempScholar.cohort, tempScholar.cwid))
        connection.commit()
    connection.close()

#ENDGAME: potentially, we can also implement a GET RID OF DUPLICATES measure in this
def getOrderId(tempScholar, tempOrder):
    connection = sqlite3.connect("scholars.db", timeout=10)
    myCursor = connection.cursor()
    returnSql = """
        SELECT order_id
        FROM Orders
        WHERE cwid = ? AND item_number = ?;
        """
    myCursor.execute(returnSql, (tempScholar.cwid, tempOrder.item_num))
    connection.commit()

    tupleOrderId = myCursor.fetchone()
    order_id = int(tupleOrderId[0])
    connection.close()
    return(order_id)
#NEED TO ADD ITEM PRICE IN HERE AS WELL!
def updateOrder(item, order_id):
    connection = sqlite3.connect("scholars.db", timeout=10)
    myCursor = connection.cursor()

    #NEED TO ADD ITEM_PRICE
    updateSql = """
        UPDATE Orders
        set item_name = ?,
            item_number = ?
        where order_id = ?
        """
    myCursor.execute(updateSql, (item['item_name'], item['item_num'], order_id))
    connection.commit()
    connection.close()

def insertOrder(tempScholar, tempOrder):
    create_table()
    connection = sqlite3.connect("scholars.db", timeout=10)
    myCursor = connection.cursor()
    insertSql = """
        INSERT INTO Orders (cwid, item_number, item_quantity) VALUES (?,?,?)
        """
    try:
        myCursor.execute(insertSql, (tempScholar.cwid, tempOrder.item_num, tempOrder.quantity))
        connection.commit()

    except:
        print ("you dumb motherfucker")

    connection.close()
"""


tempScholar = Scholar(879433452, "Jason", "Jose", "Cohort 1 (2017)")
tempOrder = Order(879433452, 123456789, 1, "https://site.com")
tempItem = {"item_num": 987654321, "item_name": "Notebook" }

insertScholar(tempScholar)
insertOrder(tempScholar, tempOrder)

print (tempOrder.item_num)
globals.order_id = getOrderId(tempScholar, tempOrder)
updateOrder(tempItem, globals.order_id)

tempScholar = Scholar(485728013, "Bobby", "Brown", "Cohort 1 (2017)")
tempOrder = Order(485728013, 483920191, 2, "https://site.com")
tempItem = {"item_num": 375829103, "item_name": "Markers" }

insertScholar(tempScholar)
insertOrder(tempScholar, tempOrder)

print (tempOrder.item_num)
globals.order_id = getOrderId(tempScholar, tempOrder)
updateOrder(tempItem, globals.order_id)
"""
