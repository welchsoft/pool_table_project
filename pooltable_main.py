from pooltable_manager import *
import os

class Main:
    def __init__(self):
        self.mystore = Manager()
        self.mystore.load_table_state()
        self.mystore.update_from_config()
        self.menu_select = ''
        self.table_pointer = ''
        self.options_input = ''
    def main_menu(self):
        os.system("clear")
        self.ascii_pool()
        self.display_hourly_rate()
        self.mystore.display_tables()
        self.menu_primary_options()
        self.menu_select = input("[Q] to Quit: ").lower()

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
        elif self.menu_select == "doge":
            self.doge_bye()
        elif self.menu_select == "cowboy":
            self.cowboy_exit()
        elif self.menu_select == "bang":
            self.bang_exit()
        else:
            self.main_menu()

    def display_hourly_rate(self):
        print(f"Hourly Rate: is ${self.mystore.hourly_rate}")

    def menu_primary_options(self):
        print("[1] rent out table: ")
        print("[2] cash out table: ")
        print("[3] close table for maintenance: ")
        print("[4] release table from maintenance: ")
        print("[5] for options menu: ")

    def options_menu(self):
        os.system("clear")
        self.display_hourly_rate()
        self.options_menu_options()
        self.menu_select = input("\t[X] to go back: ").lower()

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
            self.menu_select = input("Are you realy sure? (yes / no): ")
            if self.menu_select.lower() == "yes":
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



    def options_menu_options(self):
        print("OPTIONS: ")
        print("\t[1] Reinitialize all tables: ")
        print("\t[2] Change Hourly Rate: ")
        print("\t[3] Change Table Count: ")
        print("\t[4] Force Reinitialize [WARNING!] will drop all table states")

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
    def ascii_pool(self):
        print("        ____")
        print("    ,dP9CGG88@b,")
        print("  ,IP  _   Y888@@b,")
        print(" dIi  (_)   G8888@b")
        print("dCII  (_)   G8888@@b")
        print("GCCIi     ,GG8888@@@")
        print("GGCCCCCCCGGG88888@@@")
        print("GGGGCCCGGGG88888@@@@...")
        print("Y8GGGGGG8888888@@@@P.....")
        print(" Y88888888888@@@@@P......")
        print(" `Y8888888@@@@@@@P'......")
        print("    `@@@@@@@@@P'.......")

    #nest other exit methods inside normal_exit YOU FOOL!
    def normal_exit(self):
        os.system("clear")
        input("hit Enter to KILL application: ")
        input("\n\n\n\n\n\n\tʕっ•ᴥ•ʔっ Goodbye friend!")
        os.system("clear")

    def cowboy_exit(self):
        os.system("clear")
        input("\n\n\n\n\n\n\n\n\n\t\t\t\tSEE YOU SPACE COWBOY...")
        os.system("clear")
    def bang_exit(self):
        os.system("clear")
        input("\n\n\n\n\n\n\n\n\n\t\t\t\tYOUR'RE GONNA CARRY THAT WEIGHT.")
        os.system("clear")
    def doge_bye(self):
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
