#import datetime
from datetime import datetime
import time
from pooltable import Pooltable
import json
import os
import smtplib
from email.message import EmailMessage

class Manager:
    def __init__(self):
        self.table_count = 12
        self.hourly_rate = 30.0
        self.table_array = []
        self.dict_array = []
        self.report_array = []
        self.config = {}
        self.flag = True
        self.total_sales = 0

#checks to make sure pool tables are cashed out before allowing a re-initialization of pool tables
# figure out on the fly pool table count changes and hourly rate changes
    def table_reset_permissions(self):
        self.flag = True
        for table in self.table_array:
            if table.status == "occupied":
                print(f"Table[{table.table_number}] is occupied cash out first!")
                self.flag = False
        if self.flag == False:
            print("Error you must cash out before proceeding")
            input()
        else:
            return True

#changes the table count, checks permission first, saves to config then re-initialized tables
    def change_table_count(self,new_table_count):
            if self.table_reset_permissions():
                self.table_count = new_table_count
                self.dump_config()
                self.set_up_tables()
                input(f"Table count is now: {self.table_count}")

#changes the hourly rate, checks permission first, saves to config then re-initialized tables
    def change_hourly_rate(self,new_hourly_rate):
        if self.table_reset_permissions():
            self.hourly_rate = new_hourly_rate
            self.dump_config()
            self.set_up_tables()
            input(f"Hourly Rate is now: ${self.hourly_rate}")

#used for reinitalization of tables, checks permission first
    def set_up_tables(self):
        if self.table_reset_permissions():
            self.table_array = []
            for index in range(1,self.table_count+1):
                self.table_array.append(Pooltable(index,"open",self.hourly_rate))
            print("I AM THE TABLE!")
            self.big_dump()

#forced re-initialize tables, NO PERMISSIONS CHECK!
    def force_set_up_tables(self):
        self.table_array = []
        for index in range(1,self.table_count+1):
            self.table_array.append(Pooltable(index,"open",self.hourly_rate))
        print("I AM THE TABLE!")
        self.big_dump()

#reads in table state from .json file, if nothing there it calls set up tables instead
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
#dumps the array and loads in the .json record, stay sour python pickle users!
        self.table_array = []
        for dict in self.dict_array:
            pooltable = Pooltable(dict["table_number"],dict["status"],dict["rate"])
            pooltable.rebuild(dict["start_stamp"],dict["start_time"],dict["end_stamp"],dict["end_time"],dict["total_stamp"],dict["total_time"],dict["sales"])
            self.table_array.append(pooltable)

#displays the tables and their state, shouldnt this be in the main menu???
    def display_tables(self):
        for table in self.table_array:
            if table.status == "occupied":
                print(f"TABLE[{table.table_number}]\t[\33[94m{table.status.upper()}\33[0m]\t[Start: {table.start_stamp}: Play Time: {round((time.time() - table.start_time)/60,2)} minutes]")
            elif table.status == "closed":
                print(f"TABLE[{table.table_number}]\t[\33[91m{table.status.upper()}\33[0m]\t[Down Since: {table.start_stamp}]")
            else:
                print(f"TABLE[{table.table_number}]\t[\33[92m{table.status.upper()}\33[0m]")

#Tried to make 2 columns, didnt work out maybe some day!
        #if len(self.table_array)%2 == 0:
        #    split_index = int(len(self.table_array)/2)
        #else:
        #    split_index = int((len(self.table_array)+1)/2)
        #for index in range(split_index):
        #    print(f"Table[{self.table_array[index].table_number}]: {self.table_array[index].status}:",end= '\t')
        #for index in range(split_index,len(self.table_array)):
        #    print(f"Table[{self.table_array[index].table_number}]: {self.table_array[index].status}:")

            #consider moving to views also show time stamps in menu

#set table to occupied
    def rent_out_table(self,table_select):
        if table_select not in range(len(self.table_array)):
            print("incorrect table number try again")
        else:
            self.table_array[table_select].occupy_table()
        self.big_dump()
#cash out occupied table
    def cash_out(self,table_select):
        if table_select not in range(len(self.table_array)):
            print("incorrect table number try again")
        else:
            self.table_array[table_select].cash_table()
            self.append_report(table_select)
        self.big_dump()
        self.total_sales_lookup()
#revive table that is in maintenance
    def open_up_table(self,table_select):
        if table_select not in range(len(self.table_array)):
            print("incorrect table number try again")
        else:
            self.table_array[table_select].open_table()
        self.big_dump()
#put a table out of its misery
    def close_table(self,table_select):
        if table_select not in range(len(self.table_array)):
            print("incorrect table number try again")
        else:
            self.table_array[table_select].close_table()
            self.append_report(table_select)
        self.big_dump()
#constructs array of dictionaries that are table objects cast to __dict__
    def table_to_dict(self):
        self.dict_array = []
        for index in range(len(self.table_array)):
            self.dict_array.append(self.table_array[index].__dict__)
#contrcuts the save state file, this keeps the state of tables between sessions
    def big_dump(self):
        self.table_to_dict()
        with open('pooltable_save_state.json','w') as file:
            file.write(json.dumps(self.dict_array,indent=2))

#makes Reports directory and generates files to it for each unique day of operation
    def generate_report(self):
        os.system("mkdir Reports")
        self.report_date = time.strftime("%m-%d-%Y")
        os.system("touch Reports/"+self.report_date+".json")
#Appends the report of the day any time it is called with new info
    def append_report(self,table_select):
        self.generate_report()

        with open("Reports/"+self.report_date+".json",'r+') as file:
            file.seek(0)
            first_char = file.read(1)
            if not first_char:
                file.write("[]")
            else:
                with open("Reports/"+self.report_date+".json") as load_report:
                    self.report_array = json.load(load_report)

        self.report_array.append(self.table_array[table_select].__dict__)

        with open("Reports/"+self.report_date+".json",'w') as report_json:
            report_json.write(json.dumps(self.report_array,indent=2))

    def total_sales_lookup(self):
        self.generate_report()

        with open("Reports/"+self.report_date+".json",'r+') as file:
            file.seek(0)
            first_char = file.read(1)
            if not first_char:
                file.write("[]")
            else:
                with open("Reports/"+self.report_date+".json") as load_report:
                    self.report_array = json.load(load_report)

        self.total_sales = 0
        for report in self.report_array:
            self.total_sales += report["sales"]

#allows the Manager to update its data from a config file
    def update_from_config(self):
        os.system("touch config.json")
        with open('config.json') as config:
            self.config = json.load(config)
            self.table_count = self.config["table_count"]
            self.hourly_rate = self.config["hourly_rate"]
#updates the config content
    def dump_config(self):
        self.config.update({"table_count":self.table_count, "hourly_rate":self.hourly_rate})
        with open('config.json','w') as config:
            config.write(json.dumps(self.config))

#send email of report for extreme hard mode
#error 61 apparently im being denied by either my ISP or by my email service
#probably for security or anti spam reasons
    def send_email(self):
        with open("Reports/"+self.report_date+".json") as fp:
            msg = EmailMessage()
            msg.set_content(fp.read())

        msg['Subject'] = 'The contents of %s' % self.report_date+".json"
#be sure not to share personal email on github
        msg['From'] = 'make up an email'
        msg['To'] = 'make up an email'

        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()
#most of the code assumes table_count will not change after set-up has already been called
