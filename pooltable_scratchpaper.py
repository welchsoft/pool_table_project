#todolist: timestamps, fileIO, mainfunction

from pooltable_manager import *

from datetime import datetime


mystore = Manager()
mystore.set_up_tables()
mystore.display_tables()
mystore.rent_out_table(2)
mystore.rent_out_table(6)
mystore.close_table(7)
mystore.display_tables()

print(datetime.now())
start = datetime.now()
input("wait a few minutes")
end = datetime.now()
print(end - start)

#split the end date time object into an array by casting it as a string
split_ends = str(end-start).split(":")

print(split_ends)

#total up the minuts by taking the [0]*60 of split result which is hours
# and adding the [1] which is minutes
minutes = (int(split_ends[0])*60) + int(split_ends[1])

print(minutes)

#divide hourly rate into minuts and multiply by minutes
cost = (30.0 / 60) * minutes

print(cost)

#ok so im set to deliver pool table number, start date time, end date time, total time, and close_table
# i need to set it up in my manager page and then rig it up for fileIO
