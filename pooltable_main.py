from pooltable_manager import *
import os
import tkinter
#import threading
#nice try but a nightmare to debug maybe next time ill have an auto refreshing page

class Main:
    def __init__(self):
        self.mystore = Manager()
        self.mystore.load_table_state()
        self.mystore.update_from_config()
        self.mystore.total_sales_lookup()
        self.menu_select = ''
        self.table_pointer = ''
        self.options_input = ''
        #self.main_flag = True
        self.pool_rotate = 0

#main "loop" for decision making, it actualy just relies on recursive calls after most choices conclude
    def main_menu(self):
        self.display_loop()
        #os.system("clear")
        #self.ascii_pool()
        #self.display_hourly_rate()
        #self.display_total_sales()
        #self.mystore.display_tables()
        #self.menu_primary_options()
        self.menu_select = input("\t[Q] to Quit: \n").lower()

        if self.menu_select == "1":
            self.mystore.rent_out_table(self.table_selecter())
            self.main_menu()

        elif self.menu_select == "2":
            self.mystore.cash_out(self.table_selecter())
            self.main_menu()

        elif self.menu_select == "3":
            self.mystore.close_table(self.table_selecter())
            self.main_menu()

        elif self.menu_select == "4":
            self.mystore.open_up_table(self.table_selecter())
            self.main_menu()

        elif self.menu_select == "5":
            self.options_menu()
            self.main_menu()

        elif self.menu_select == "q":
            self.normal_exit()

        else:
            self.main_menu()

    def display_loop(self):
        #threading.Timer(10.0, self.display_loop).start()
        os.system("clear")
        self.ascii_pool()
        self.display_hourly_rate()
        self.display_total_sales()
        self.mystore.display_tables()
        self.menu_primary_options()

#maybe this will be expanded later, for now its a glorified print statement
    def display_hourly_rate(self):
        print(f"\n[Hourly Rate: is ${self.mystore.hourly_rate}]")

#maybe this will be expanded later, for now its a glorified print statement
    def display_table_count(self):
        print(f"[Table Count: is {self.mystore.table_count}]")

#maybe this will expand later, for now its a glofified print statement
    def display_total_sales(self):
        print(f"Todays Total Sales: ${self.mystore.total_sales}")
        print("==========================================")

#options for the main menu
    def menu_primary_options(self):
        print("==================[MENU]==================")
        print("\t[1] Rent out table: ")
        print("\t[2] Cash out table: ")
        print("\t[3] Close table for maintenance: ")
        print("\t[4] Release table from maintenance: ")
        print("\t[5] Options menu: ")
        print("\t[Enter] Refresh Page: ")

#options options menu side path off the main menu
    def options_menu(self):
        os.system("clear")
        self.display_hourly_rate()
        self.display_table_count()
        self.options_menu_options()
        self.menu_select = input("\t[X] to go back: \n").lower()

        if self.menu_select == "1":
            self.mystore.set_up_tables()
            self.options_menu()

        elif self.menu_select == "2":
            self.mystore.change_hourly_rate(self.options_input_validator())
            self.options_menu()

        elif self.menu_select == "3":
            self.mystore.change_table_count(self.options_input_validator())
            self.options_menu()

        elif self.menu_select == "4":
            self.menu_select = input("Are you realy sure? This is the Nuclear option! (yes / no): ").lower()
            if self.menu_select == "yes":
                self.mystore.force_set_up_tables()
                input()
            else:
                print("that was a close one! ")
                input()
            self.options_menu()

        elif self.menu_select == "x":
            pass

        else:
            self.options_menu()


#displays the options available in the options menu
    def options_menu_options(self):
        print("==================[OPTIONS]==================")
        print("\t[1] Reinitialize all tables: ")
        print("\t[2] Change Hourly Rate: ")
        print("\t[3] Change Table Count: ")
        print("\t[4] Force Reinitialize [WARNING!] will drop all table states")

#used for most main menu choices
    def table_selecter(self):
        while True:
            self.table_pointer = int(input("Enter Table number: "))-1
            try:
               self.table_pointer in range(len(self.mystore.table_array))
            except ValueError:
               print('Error: invalid number ')
               continue
            if self.table_pointer in range(len(self.mystore.table_array)):
                return self.table_pointer
                break
            else:
               print(f"must be a number between 1 and {len(self.mystore.table_array)}:")

#just making sure you input a number for the hourly rate and table count
    def options_input_validator(self):
        while True:
            self.options_input = input("Enter number: ")
            try:
               self.options_input = int(self.options_input)
            except ValueError:
               print('Error: invalid input ')
               continue
            if 1 <= self.options_input:
                return self.options_input
                break
            else:
               print("must be a number:")

#the logo how spiffy!
    def ascii_pool(self):
        if self.pool_rotate == 5:
            self.pool_rotate = 0
            print("\t        ____")
            print("\t    ,dP9CGG88@b,")
            print("\t  ,IPC888888888@@b,")
            print("\t dIi8888888888888@b")
            print("\tdCIIGGGGGG8888888@@b")
            print("\tGCCIICCCCCCCG8888@@@")
            print("\tGGCCCCCCCGGG88888@@@")
            print("\tGGGGCCCGGGG88888@@@@...")
            print("\tY8GGGGGG8888888@@@@P.....")
            print("\t Y88888888888@@@@@P......")
            print("\t `Y8888888@@@@@@@P'......")
            print("\t    `@@@@@@@@@P'.......")
        else:
            print("\t        ____")
            print("\t    ,dP9CGG88@b,")
            print("\t  ,IP  _   Y888@@b,")
            print("\t dIi  (_)   G8888@b")
            print("\tdCII  (_)   G8888@@b")
            print("\tGCCIi     ,GG8888@@@")
            print("\tGGCCCCCCCGGG88888@@@")
            print("\tGGGGCCCGGGG88888@@@@...")
            print("\tY8GGGGGG8888888@@@@P.....")
            print("\t Y88888888888@@@@@P......")
            print("\t `Y8888888@@@@@@@P'......")
            print("\t    `@@@@@@@@@P'.......")

        self.pool_rotate += 1
#got a bit carried away with easter egg exits
#nest other exit methods inside normal_exit YOU FOOL!
    def normal_exit(self):
        os.system("clear")
        self.menu_select = input("hit Enter to KILL application: ").lower()
        if self.menu_select == "doge":
            self.doge_exit()

        elif self.menu_select == "cowboy":
            self.cowboy_exit()

        elif self.menu_select == "bang":
            self.bang_exit()

        elif self.menu_select == "tkin":
            self.tkin_try()
        else:
            input("\n\n\n\n\n\n\t\tʕっ•ᴥ•ʔっ Goodbye friend!")
        os.system("clear")

    def cowboy_exit(self):
        os.system("clear")
        input("\n\n\n\n\n\n\n\n\n\t\t\t\tSEE YOU SPACE COWBOY...")
        os.system("clear")
    def bang_exit(self):
        os.system("clear")
        input("\n\n\n\n\n\n\n\n\n\t\t\t\tYOUR'RE GONNA CARRY THAT WEIGHT.")
        os.system("clear")
    def doge_exit(self):
        os.system("clear")
        print("░░░░░░░░░▄░░░░░░░░░░░░░░▄")
        print("░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌")
        print("░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐")
        print("░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐")
        print("░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐")
        print("░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌")
        print("░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌")
        print("░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐")
        print("░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌")
        print("░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌")
        print("▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐")
        print("▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌")
        print("▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐")
        print("░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌")
        print("░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐")
        print("░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌")
        print("░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀")
        print("░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀")
        print("░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀")
        input("ok?")
        os.system("clear")

    def tkin_try(self):
        top = tkinter.Tk()
        doge = "WHAT HAVE YOU DONE?"
        msg = tkinter.Message(top, text = doge)
        msg.pack()
        top.mainloop()
