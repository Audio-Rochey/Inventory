# Inventory
Python Scripts and MySQL Database

At Expat Audio, I keep an inventory of all parts that stores details about the parts and their location.
The mysql database is kept remotely, and is logged into using Putty, with a method called SSHTunneling. 
It allows applications to think that the database is on the localhost.

In the Repo, there is:

1) Example of the database in excel format (so you can see the headers etc)
2) Python 2.7 app that can connected, lookup and print a Zebra LP2824 label to go on the front of boxes
3) Python app to bulk-add PID's drawers into storage unit.
