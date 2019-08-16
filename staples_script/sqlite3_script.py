import sqlite3



connection = sqlite3.connect("scholars.db", timeout=10)
myCursor = connection.cursor()

dropCommand = """DROP TABLE IF EXISTS Scholars"""
myCursor.execute(dropCommand)
connection.commit()

scholars_sql = """
CREATE TABLE Scholars
    (
    cwid integer PRIMARY KEY,
    first_name varchar(20) ,
    last_name varchar(20),
    acct_balance real ,
    cohort varchar(20)
    )
    """
myCursor.execute(scholars_sql)

dropCommand = """DROP TABLE IF EXISTS Orders"""
myCursor.execute(dropCommand)
connection.commit()
orders_sql = """
CREATE TABLE Orders
    (
    cwid integer PRIMARY KEY,
    item_number integer ,
    item_name varchar(20) ,
    item_price real ,
    item_quantity integer
    )
    """
myCursor.execute(orders_sql)



myCursor.execute("""INSERT INTO Orders (cwid,item_price) VALUES (889456472, 100.00)""")
connection.commit()
connection.close()
