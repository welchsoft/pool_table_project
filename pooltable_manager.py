import datetime
from datetime import datetime
import time

class Pooltable:
    def __init__(self, tablenumber, status, rate):
        self.tablenumber = tablenumber
        self.status = status
        self.start_time = 0
        self.end_time = 0
        self.total_time = 0
        self.rate = rate
        self.cost = 0.0

    def occupy_table(self):
        if self.status == "open":
            self.status = "occupied"
            print(f"table[{self.tablenumber+1}] is now occupied!")
            self.start_time = datetime.now()

    def open_table(self):
        if self.status == "occupied" or self.status == "closed":
            self.status = "open"
            print(f"table[{self.tablenumber+1}] is now open!")
            self.end_time = datetime.now()
            self.total_time = self.end_time - self.start_time
            #self.cost =

    def close_table(self):
        if self.status == "open":
            self.status = "closed"
            print(f"table[{self.tablenumber+1}] is down for maintenance!")
        elif self.status == "closed":
            print(f"table[{self.tablenumber+1}] is already closed!")
        elif self.status == "occupied":
            print("Table occupied it must be opened first")

class Manager:
    def __init__(self):
        self.table_count = 12
        self.hourly_rate = 30
        self.table_array = []

    def change_table_count(self,new_table_count):
        self.table_count = new_table_count

    def change_hourly_rate(self,new_hourly_rate):
        self.hourly_rate = new_hourly_rate

    def set_up_tables(self):
        for index in range(0,self.table_count):
            self.table_array.append(Pooltable(index,"open",self.hourly_rate))

    def display_tables(self):
        for table in self.table_array:
            print(f"Table[{table.tablenumber+1}]: {table.status}: I AM THE TABLE!")

    def rent_out_table(self,table_select):
        self.table_array[table_select].occupy_table()

    def close_table(self,table_select):
        self.table_array[table_select].close_table()
