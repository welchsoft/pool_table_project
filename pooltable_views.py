from pooltable_manager import *
import os

def main_menu():
    mystore = Manager()
    mystore.set_up_tables()
    menu_select = ''
    while menu_select != "q":
        os.system("clear")
        mystore.display_tables()
        menu_select = input("q to quit: ").lower()


main_menu()
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
