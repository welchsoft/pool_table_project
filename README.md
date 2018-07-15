# Pool hall app

a pool hall management app, based on an old request from the University of Houston cougar lounge, written in python.


the hourly rate and pool table count can be written to and read from a config file.

tables can be checked out to guests, locked down for maintenance, opened up for rental, or cashed out.

the current state of all tables is displayed in the command console, this will and can be refreshed by all table state changes.
you can manualy refresh with any entty that is not reserved.

current state of the pool tables are stored to a file any time a table changes its state. this state is read on start up,
this state can dumped if neccessary.

any change that would result in a loss of table states, requires that all tables be cashed out first. 
unless specified if neccessary, this comes with a warning.

cashing out a table will append to a transactions file generated for that day.

exiting requires confirmation, secret codes can be entered for some fun special exit messages.
