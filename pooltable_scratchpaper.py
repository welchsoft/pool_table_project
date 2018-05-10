from pooltable_manager import *

from datetime import datetime
import time


mystore = Manager()
mystore.set_up_tables()
mystore.display_tables()
mystore.rent_out_table(2)
mystore.rent_out_table(6)
mystore.close_table(7)
mystore.display_tables()
input("wait a few minutes")
mystore.cash_table(6)
#mystore.generate_report()


#ok so im set to deliver pool table number, start date time, end date time, total time, and close_table
# i need to set it up in my manager page and then rig it up for fileIO
