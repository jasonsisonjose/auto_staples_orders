import gspread
from oauth2client.service_account import ServiceAccountCredentials
from staples_script.spiders import StaplesSpider
class Scholar():
    def __init__(self, cwid, first_name, last_name, cohort):
        self.cwid = cwid
        self.first_name = first_name
        self.last_name = last_name
        self.cohort = cohort

class Order():
    def __init__(self, cwid, item_num, quantity, item_link):
        self.cwid = cwid
        self.item_num = item_num
        self.quantity = quantity
        self.item_link = item_link

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
workSheet = client.open("Staple_Order_Request").sheet1

# Extract and print each row
#row_num is 2 because the first row is just the variable names, so the data we want actuallt starts on row 2
row_num = 2
#this while condition loops until it goes to the end of the number of rows
while row_num < workSheet.row_count:
    #if the returned list is empty, that means there is no data for us to use, so don't loop anymore
    if workSheet.row_values(row_num) == []:
        break
    #if the returned list is NOT empt, then save that list under the variable record
    record = workSheet.row_values(row_num)
    #the way I have it set up, the 5th index is the URL Item Link, so it checks if it is a valid link for staples advantage

    if record[5].find("advantage") != -1:
        tempCwid = record[2]
        tempFN = record[3]
        tempLN = record[4]
        tempCohort = record[8]
        tempScholar = Scholar(tempCwid, tempFN, tempLN, tempCohort)
        print (tempScholar.__dict__)
        print ("Hey good job, this is a valid link")
        #insert into the database, if it is already there then so the program knows that the order belongs to this scholar

        tempItem_num = record[6]
        tempQuantity = record[7]
        tempItem_link = record[5]

        tempOrder = Order(tempCwid, tempItem_num, tempQuantity, tempItem_link)
        #insert tempCwid and tempQuantity in the database

        #use the item link to activate the spider and grab Staples Information
        StaplesSpider.start_urls.append("this shit")
    else:
        print("\nYou aren't simply a clown, for you are the entire circus. Learn to copy and paste a fucking link")
    #this for loop, gets the attributes of the records one by one.
    row_num += 1
