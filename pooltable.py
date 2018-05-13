#import datetime
from datetime import datetime
import time

class Pooltable:
    def __init__(self, table_number, status, rate):
        self.table_number = table_number
        self.status = status
        self.start_stamp = ''
        self.start_time = 0
        self.end_stamp = ''
        self.end_time = 0
        self.total_stamp = ''
        self.total_time = 0
        self.rate = rate
        self.sales = 0.0

#sets table to occupied, and time values for start time /stamp
    def occupy_table(self):
        if self.status == "open":
            self.status = "occupied"
            self.start_stamp = str(datetime.now())
            self.start_time = time.time()
            print(f"table[{self.table_number}] is now occupied!")
        else:
            print("Error: invalid table status ")
            input()

#opens the table and generates time values and stamps for end / total
    def open_table(self):
        if self.status == "occupied":
            self.status = "open"
            self.end_stamp = str(datetime.now())
            self.end_time = time.time()
            self.total_time = self.end_time - self.start_time
            self.total_stamp = str(round((self.total_time)/60,2))+" minutes"
            print(f"table[{self.table_number}] is now available!")
        elif self.status == "closed":
            self.status = "open"
            print(f"Table[{self.table_number}] back online! ")
            input()
        else:
            print("Table is already open: ")
            input()
#used for cashing tables, checks permission then calls open_table
    def cash_table(self):
        if self.status == "occupied":
            self.open_table()
            self.sales = round((self.rate/60) * (self.total_time/60),2)
            print(f"The due for Table[{self.table_number}]: ${self.sales} [̲̅$̲̅(̲̅ιο̲̅̅)̲̅$̲̅]")
            input("cash out customer then hit Enter")
        else:
            print("Error: invalid table status ")
            input()
#closes table for maintenance, checks status first
    def close_table(self):
        if self.status == "open":
            self.status = "closed"
            self.start_stamp = str(datetime.now())
            print(f"table[{self.table_number}] is down for maintenance!")
            input()
        elif self.status == "closed":
            print(f"table[{self.table_number}] is already closed!")
            input()
        elif self.status == "occupied":
            self.cash_table()
#needed to load from file the state of all atributes that are not set up on instantiation
    def rebuild(self,start_stamp,start_time,end_stamp,end_time,total_stamp,total_time,sales):
        self.start_stamp = start_stamp
        self.start_time = start_time
        self.end_stamp = end_stamp
        self.end_time = end_time
        self.total_stamp = total_stamp
        self.total_time = total_time
        self.sales = sales
