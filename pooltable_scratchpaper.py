from pooltable_manager import *

from datetime import datetime
import time


mystore = Manager()
#mystore.update_from_config()
mystore.load_table_state()
mystore.set_up_tables()
mystore.display_tables()
mystore.rent_out_table(2)
mystore.rent_out_table(6)
mystore.close_table(7)
mystore.display_tables()
input("wait a few minutes")
mystore.cash_out(6)
mystore.table_to_dict()
mystore.close_table(43)
mystore.big_dump()
mystore.generate_report()
mystore.rent_out_table(4)
mystore.rent_out_table(3)
mystore.cash_out(4)
mystore.big_dump()
mystore.load_table_state()
mystore.big_dump()
#mystore.dump_config()
#mystore.change_hourly_rate(50.0)
print(mystore.hourly_rate)



#ok so im set to deliver pool table number, start date time, end date time, total time, and close_table
# i need to set it up in my manager page and then rig it up for fileIO
