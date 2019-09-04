
global order_id
order_id = 0



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
