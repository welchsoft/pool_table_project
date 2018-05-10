import datetime
from datetime import datetime
import time

class Pooltable:
    def __init__(self, tablenumber, status, rate):
        self.tablenumber = tablenumber
        self.status = status
        self.start_time = 0
        self.start_stamp = 0
        self.end_time = 0
        self.end_stamp = 0
        self.total_time = 0
        self.total_stamp = 0
        self.rate = rate
        self.cost = 0.0

    def occupy_table(self):
        if self.status == "open":
            self.status = "occupied"
            print(f"table[{self.tablenumber+1}] is now occupied!")
            self.start_stamp = datetime.now()
            self.start_time = time.time()


    def open_table(self):
        if self.status == "occupied" or self.status == "closed":
            self.status = "open"
            print(f"table[{self.tablenumber+1}] is now available!")
            self.end_stamp = datetime.now()
            self.total_stamp = self.end_stamp - self.start_stamp
            self.end_time = time.time()
            self.total_time = self.end_time - self.start_time
            self.cost = (self.rate/60) * (self.total_time/60)
            print(f"The due for Table[{self.tablenumber+1}]: ${round(self.cost,2)}")

    def close_table(self):
        if self.status == "open":
            self.status = "closed"
            print(f"table[{self.tablenumber+1}] is down for maintenance!")
        elif self.status == "closed":
            print(f"table[{self.tablenumber+1}] is already closed!")
        elif self.status == "occupied":
            print("Table occupied it must be opened first")

    def report(self):
        pass
