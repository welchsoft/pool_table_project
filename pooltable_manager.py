#import datetime
from datetime import datetime
import time
from pooltable import Pooltable
import json
import os

class Manager:
    def __init__(self):
        self.table_count = 12
        self.hourly_rate = 30.0
        self.table_array = []
        self.dict_array = []
        self.report_array = []
        self.config = {}

    def change_table_count(self,new_table_count):
        self.table_count = new_table_count
        self.dump_config()
        self.table_array = []
        #warn user this will destroy the tables

    def change_hourly_rate(self,new_hourly_rate):
        self.hourly_rate = new_hourly_rate
        self.dump_config()

#set up the tables, figure out how to modify for saves, and on the fly pool table count changes
    def set_up_tables(self):
        for index in range(1,self.table_count+1):
            self.table_array.append(Pooltable(index,"open",self.hourly_rate))
        print("I AM THE TABLE!")

    def load_table_state(self):
        os.system("touch pooltable_save_state.json")
        with open('pooltable_save_state.json') as file:
            file.seek(0)
            first_char = file.read(1)
            if not first_char:
                self.set_up_tables()
                return
            else:
                with open('pooltable_save_state.json') as load_table:
                    self.dict_array = json.load(load_table)

        self.table_array = []
        for dict in self.dict_array:
            pooltable = Pooltable(dict["table_number"],dict["status"],dict["rate"])
            pooltable.rebuild(dict["start_stamp"],dict["start_time"],dict["end_stamp"],dict["end_time"],dict["total_stamp"],dict["total_time"],dict["cost"])
            self.table_array.append(pooltable)

    def display_tables(self):
        for table in self.table_array:
            print(f"Table[{table.table_number}]: {table.status}:")

            #consider moving to views also show time stamps in menu

    def rent_out_table(self,table_select):
        if table_select not in range(len(self.table_array)):
            print("incorrect table number try again")
        else:
            self.table_array[table_select].occupy_table()
        self.big_dump()

    def cash_out(self,table_select):
        if table_select not in range(len(self.table_array)):
            print("incorrect table number try again")
        else:
            self.table_array[table_select].cash_table()
            self.append_report(table_select)
        self.big_dump()

    def open_up_table(self,table_select):
        if table_select not in range(len(self.table_array)):
            print("incorrect table number try again")
        else:
            self.table_array[table_select].open_table()
        self.big_dump()

    def close_table(self,table_select):
        if table_select not in range(len(self.table_array)):
            print("incorrect table number try again")
        else:
            self.table_array[table_select].close_table()
        self.big_dump()

    def table_to_dict(self):
        self.dict_array = []
        for index in range(len(self.table_array)):
            self.dict_array.append(self.table_array[index].__dict__)

    def big_dump(self):
        self.table_to_dict()
        with open('pooltable_save_state.json','w') as file:
            file.write(json.dumps(self.dict_array,indent=2))

    def generate_report(self):
        self.report_date = time.strftime("%m-%d-%Y")
        os.system("touch "+self.report_date+".json")

    def append_report(self,table_select):
        self.generate_report()

        with open(self.report_date+".json",'r+') as file:
            file.seek(0)
            first_char = file.read(1)
            if not first_char:
                file.write("[]")
            else:
                with open(self.report_date+".json") as load_report:
                    self.report_array = json.load(load_report)

        self.report_array.append(self.table_array[table_select].__dict__)

        with open(self.report_date+".json",'w') as report_json:
            report_json.write(json.dumps(self.report_array,indent=2))

    def update_from_config(self):
        os.system("touch config.json")
        with open('config.json') as config:
            self.config = json.load(config)
            self.table_count = self.config["table_count"]
            self.hourly_rate = self.config["hourly_rate"]

    def dump_config(self):
        self.config.update({"table_count":self.table_count, "hourly_rate":self.hourly_rate})
        with open('config.json','w') as config:
            config.write(json.dumps(self.config))

#known shortcomings: set up tables is not savestate ready
#most of the code assumes table_count will not change after set-up has already been called
