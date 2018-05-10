import datetime
from datetime import datetime
import time
from pooltable import Pooltable
import json

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
        print("I AM THE TABLE!")

    def display_tables(self):
        for table in self.table_array:
            print(f"Table[{table.tablenumber+1}]: {table.status}:")

            #consider moving to views also show time stamps in menu

    def rent_out_table(self,table_select):
        self.table_array[table_select].occupy_table()

    def cash_table(self,table_select):
        self.table_array[table_select].open_table()

    def close_table(self,table_select):
        self.table_array[table_select].close_table()
