import gspread
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from oauth2client.service_account import ServiceAccountCredentials
from globals import Scholar, Order
import globals
from sqlite3_script import insertScholar, insertOrder, getOrderId


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
workSheet = client.open("Staple_Order_Request").sheet1

# item index is a dynamic dictionary that stores the variable_names and connects it to the index it is located at
# this is so I don't have to use integers for the indices and can be more flexible by just using variable names
item_index = {}
index = 0
for variable_name in workSheet.row_values(1):
    var_underscore = variable_name.replace(" ", "_")
    item_index.update({})
    item_index[var_underscore] = index
    index += 1

for key in item_index:
    print (key, item_index[key])
tempItem_list = []
# Extract and print each row
# the first row is just variable names, so we want the 2nd row
row_num = 2
#this while condition loops until it goes to the end of the number of rows
while row_num < workSheet.row_count:

    #if the returned list is empty, that means there is no data for us to use, so don't loop anymore
    if workSheet.row_values(row_num) == []:
        break
    #if the returned list is NOT empty, then save that list under the variable record
    record = workSheet.row_values(row_num)

    #if the item link has the word "advantage", in it, it is now considered a valid link
    if record[item_index["Item_Link"]].find("advantage") != -1:
        tempCwid = record[item_index["CWID"]]
        tempFN = record[item_index["First_Name"]]
        tempLN = record[item_index["Last_Name"]]
        tempCohort = record[item_index["Cohort"]]
        tempScholar = Scholar(tempCwid, tempFN, tempLN, tempCohort)
        print ("Hey good job, this is a valid link")

        insertScholar(tempScholar)

        #insert into the database, if it is already there then so the program knows that the order belongs to this scholar

        tempItem_num = record[item_index["Item_Number"]]
        tempQuantity = record[item_index["Quantity_of_Desired_Items"]]
        tempItem_link = record[item_index["Item_Link"]]
        tempOrder = Order(tempCwid, tempItem_num, tempQuantity, tempItem_link)
        #insert tempCwid and tempQuantity in the database
        insertOrder(tempScholar, tempOrder)
        globals.order_id = getOrderId(tempScholar, tempOrder)

        tempItem_list.append(tempItem_link)
        print ("THIS IS THE MOTHERFUCKING LIST: ",tempItem_list)
        #use the item link to activate the spider and grab Staples Information
        process = CrawlerProcess(get_project_settings())

        # 'staples' is the name of one of the spiders of the project.
        #start_urls must be a list not a string!
        process.crawl('staples', start_urls= tempItem_list)
        tempItem_list.pop(0)
    else:
        print("\nYou aren't simply a clown, for you are the entire circus. Learn to copy and paste a fucking link")

    #this for loop, gets the attributes of the records one by one.
    row_num += 1
process.start() # the script will block here until the crawling is finished
