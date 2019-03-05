# this program is designed to take a PID and print desired duplicates.
# printing sequentially can be done using the lbl file and zebra designer.
# This code only works for windows and cannot find the system printers in linux or mac

# dev version trying to add an image of the label

This is designed for Python 2.7

import os, sys
import csv #added for csv support
import MySQLdb as mdb
import win32print # added for windows 10 - in hope!

import win32print
from zebra import zebra
from Tkinter import *

#added to add the image
#http://stackoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter-python-2-7

from PIL import ImageTk, Image
path = 'EA-PID2-example.png'



root = Tk()
root.title("Print a PID Barcode")
#Creating the entries
e1 = Entry(root)
e2 = Entry(root)
v = IntVar()
v.set(1)  # initializing the choice, i.e. Python

global txttoprint 
global PIDtoprint 



printer_info = win32print.EnumPrinters (
   win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS
)
printer_names = [name for (flags, description, name, comment) in 
printer_info]
#for i, name in enumerate (printer_names):
#   print ("%d) %s" % (i + 1, name))



def ShowChoice(): #show choice in debug terminal
    #print v.get()
	n_printer = v.get()
	printer_name = printer_names[n_printer]
	print ("Using %s" % printer_name)
	#print ("""Using""", printer_name)
	#z.setqueue(printer_name)
	return
	
def gettxttoprint(txttoprint, PIDtoprint):
        #Most of this code comes from: http://zetcode.com/db/mysqlpython/
        pidsearch = PIDtoprint
        print "PID passed to gettxttoprint= %s." % pidsearch
        print "current value of txttoprint= %s." % txttoprint
        try:
                con = mdb.connect(host="localhost",user="thisisademo",
                passwd="thisisademo",db="thisisademo");

                cur = con.cursor(mdb.cursors.DictCursor)

                cur.execute("SELECT `Product ID`,`STORAGELABEL` FROM `TABLE 1` WHERE `Product ID` LIKE (%s)", (pidsearch))
                ver = cur.fetchone()
    

                lookuprodid = ver["Product ID"]
                txttoprint = ver["STORAGELABEL"]
                print "PID returned from mysql= %s." % lookuprodid
                print "Storage label text is= %s." % txttoprint
    


    
        except mdb.Error, e:
                print "Error %d: %s" % (e.args[0],e.args[1])
                sys.exit(1)
    
        finally:    
        
            if con:    
                con.close()

        return (txttoprint)

def print_oneline_zebra():
        PIDtoprint = e2.get()
        txttoprint="printonelinzebrafunction"
        print(txttoprint)
        txttoprint = gettxttoprint(txttoprint, PIDtoprint)
        print(txttoprint)



        n_printer = v.get()
        printer_name = printer_names[n_printer]
        # test to see if it knowns the right printer.
        print ("Using %s" % printer_name)
        
        print (txttoprint)
        print (PIDtoprint)
        #Set up the printer and go!
        z = zebra()
        z.setqueue(printer_name)

        label="""
N
B50,25,0,1,2,6,34,B,"%s"
A200,60,0,2,1,1,N,"EA PID"
A50,3,0,2,1,1,N,"%s"
P1

	""" %(PIDtoprint, txttoprint)
        #End of EPL commands to print PID tag
        z.setqueue(printer_name)
        z.output(label)
        print ("Print Complete")
        return

	
#formatting the GUI starts here.


#add the image
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image = img)
panel.pack(side = "top", fill = "both", expand = "yes")



Label(root, 
      text="""Type the PID:""",
      justify = LEFT,
      padx = 20).pack()

e2.pack()

#Adds the button
Button(root, text='Print', command=print_oneline_zebra).pack()

# Adds the text to add a button
Label(root, 
      text="""Choose your favourite printer:""",
      justify = LEFT,
      padx = 20).pack(side=LEFT)

#Adds the radio buttons	  
for val, txt in enumerate (printer_names):
    Radiobutton(root, 
                text=txt,
                padx = 20, 
                variable=v, 
                command=ShowChoice,
                value=val).pack(anchor=W)

#adds the button   
Label(root, 
      text="""Make sure you are connected via Putty on your local machine!""",
      justify = LEFT,
      pady = 50).pack()


#e1.pack()



mainloop()

