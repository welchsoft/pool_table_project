from pooltable_manager import *
import os

class Main:
    def __init__(self):
        self.mystore = Manager()
        self.mystore.set_up_tables()
        self.menu_select = ''
    def main_menu(self):
        os.system("clear")
        self.mystore.display_tables()
        self.menu_select = input("[Q] to Quit: ").lower()




        if self.menu_select.lower() == "q":
            self.normal_exit()
        elif self.menu_select.lower() == "doge":
            self.doge_bye()
        elif self.menu_select.lower() == "cowboy":
            self.cowboy_exit()
        elif self.menu_select.lower() == "bang":
            self.bang_exit()
        else:
            self.main_menu()











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
