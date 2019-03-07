# Current sandbox project to make a prog that
# connects to the database, requests a box number, then lets you scan item after item.
# 3/3/2019
# this website was very helpful: http://zetcode.com/python/pymysql/
# Added voice playback for PID's


import pymysql
from gtts import gTTS
from playsound import playsound
import pyglet
from time import sleep
import os


con = pymysql.connect(
    host="localhost",
    user="eainventoryadmin",
    passwd="eainventoryadmin",
    db="expataudioinventory",
    charset= "utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

print("****     MAKE SURE PUTTY IS CONNECTED TO THE SERVER!    ****")
print("**** This Program is to update the location of products ****")
print("")

storageidtoupdate = input('Whats the name of the storage? ')
loopkeep = 1





var = 1
global count
count = 0

while var == 1 :
    pidsearch = input('Enter PID in PIDxxxxx format ')
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
