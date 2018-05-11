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
        self.cost = 0.0

    def occupy_table(self):
        if self.status == "open":
            self.status = "occupied"
            print(f"table[{self.table_number}] is now occupied!")
            self.start_stamp = str(datetime.now())
            self.start_time = time.time()


    def open_table(self):
        if self.status == "occupied":
            self.status = "open"
            print(f"table[{self.table_number}] is now available!")
            self.end_stamp = str(datetime.now())
            self.end_time = time.time()
            self.total_time = self.end_time - self.start_time
            self.total_stamp = str(round((self.total_time)/60,2))+" minutes"
        elif self.status == "closed":
            self.status = "open"

    def cash_table(self):
        self.open_table()
        self.cost = round((self.rate/60) * (self.total_time/60),2)
        print(f"The due for Table[{self.table_number+1}]: ${self.cost} [̲̅$̲̅(̲̅ιο̲̅̅)̲̅$̲̅]")

    def close_table(self):
        if self.status == "open":
            self.status = "closed"
            print(f"table[{self.table_number}] is down for maintenance!")
        elif self.status == "closed":
            print(f"table[{self.table_number}] is already closed!")
        elif self.status == "occupied":
            print("Table occupied it must be opened first")

    def rebuild(self,start_stamp,start_time,end_stamp,end_time,total_stamp,total_time,cost):
        self.start_stamp = start_stamp
        self.start_time = start_time
        self.end_stamp = end_stamp
        self.end_time = end_time
        self.total_stamp = total_stamp
        self.total_time = total_time
        self.cost = cost
