# Current sandbox project to make a prog that
# connects to the database, requests a box number, then lets you scan item after item.
# 3/3/2019
# this website was very helpful: http://zetcode.com/python/pymysql/
# Added voice playback for PID's
# Moved database credentials to pymysqllogin.cnf

# Current sandbox project to make a prog that
# connects to the database, requests a box number, then lets you scan item after item.
# 3/3/2019
# this website was very helpful: http://zetcode.com/python/pymysql/
# Added voice playback for PID's
# Moved database credentials to pymysqllogin.cnf
# 3/14/19 Databse updated to support a separate field for sample and bulk storage
# This file is for bulk

import pymysql
from gtts import gTTS
from playsound import playsound
# import pyglet
from time import sleep
import os
from configparser import ConfigParser

config = ConfigParser()
config.read("pymysqllogin.cnf")
mysqluser = config.get('mysqlinfo', 'user')
mysqlpasswd = config.get('mysqlinfo', 'passwd')
mysqlhost = config.get('mysqlinfo', 'host')
mysqldb = config.get('mysqlinfo', 'db')

con = pymysql.connect(
    host=mysqlhost,
    user=mysqluser,
    passwd=mysqlpasswd,
    db=mysqldb,
    charset= "utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

print("****     This Item is for BULK storage only!            ****")
print("****     MAKE SURE PUTTY IS CONNECTED TO THE SERVER!    ****")
print("**** This Program is to update the location of products ****")
print("**** Press q to quit                                    ****")
print("")

storageidtoupdate = raw_input('Whats the name of the storage? ')
loopkeep = 1





var = 1
global count
count = 0

while var == 1 :
    #Python 3 just uses "input" whilst Python 2.7 uses raw_input
    pidsearch = raw_input('Enter PID in PIDxxxxx format ')
    if pidsearch == "q":
        break
    with con.cursor() as cursor:
        try:

            mods = ((storageidtoupdate), (pidsearch))
            sql = """UPDATE `TABLE 1` SET `Bulk_Storage_ID`=%s  WHERE `Product ID` LIKE %s"""
            cursor.execute(sql, mods)

            print("Successfully Updated...")
            str1 = pidsearch
            str2 = str1.lstrip("PID0")
            str3 = str2.lstrip("0")
            str4 = "PID" + str3 + "Updated"
            tts = gTTS(text=str4, lang='en')
            filename = "PIDUPDATED" + str(count) + ".mp3"
            tts.save(filename)
            tts.save("temp.mp3")
            print("file saved")
            playsound(filename)
            os.remove(filename)  # remove temperory file
            print("file removed")
            count += 1
            con.commit()

        except:
            print("Oops! Something wrong")
            tts = gTTS(text="Oops! Something Wrong!", lang='en')
            playsound("win31.mp3")


        #finally:
         #   con.close()

import pymysql
from gtts import gTTS
from playsound import playsound
import pyglet
from time import sleep
import os
from configparser import ConfigParser

config = ConfigParser()
config.read("pymysqllogin.cnf")
mysqluser = config.get('mysqlinfo', 'user')
mysqlpasswd = config.get('mysqlinfo', 'passwd')
mysqlhost = config.get('mysqlinfo', 'host')
mysqldb = config.get('mysqlinfo', 'db')

con = pymysql.connect(
    host=mysqlhost,
    user=mysqluser,
    passwd=mysqlpasswd,
    db=mysqldb,
    charset= "utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

print("****     MAKE SURE PUTTY IS CONNECTED TO THE SERVER!    ****")
print("**** This Program is to update the location of products ****")
print("**** Press q to quit                                    ****")
print("")

storageidtoupdate = input('Whats the name of the storage? ')
loopkeep = 1





var = 1
global count
count = 0

while var == 1 :
    pidsearch = input('Enter PID in PIDxxxxx format ')
    if pidsearch == "q":
        break
    with con.cursor() as cursor:
        try:

            mods = ((storageidtoupdate), (pidsearch))
            sql = """UPDATE `TABLE 1` SET `Storage ID`=%s  WHERE `Product ID` LIKE %s"""
            cursor.execute(sql, mods)

            print("Successfully Updated...")
            str1 = pidsearch
            str2 = str1.lstrip("PID0")
            str3 = str2.lstrip("0")
            str4 = "PID" + str3 + "Updated"
            tts = gTTS(text=str4, lang='en')
            filename = "PIDUPDATED" + str(count) + ".mp3"
            tts.save(filename)
            tts.save("temp.mp3")
            print("file saved")
            playsound(filename)
            os.remove(filename)  # remove temperory file
            print("file removed")
            count += 1
            con.commit()

        except:
            print("Oops! Something wrong")
            tts = gTTS(text="Oops! Something Wrong!", lang='en')
            playsound("win31.mp3")


        #finally:
         #   con.close()
