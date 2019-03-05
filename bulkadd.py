# Current sandbox project to make a prog that
# connects to the database, requests a box number, then lets you scan item after item.
# 3/3/2019


import pymysql

con = pymysql.connect(
    host="localhost",
    user="thisisjustademo",
    passwd="thisisalsoademo",
    db="ofremoteinventory",
    charset= "utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

print("****     MAKE SURE PUTTY IS CONNECTED TO THE SERVER!    ****")
print("**** This Program is to update the location of products ****")
print("")

storageidtoupdate = raw_input('Whats the name of the storage? ')
loopkeep = 1


var = 1
while var == 1 :
    pidsearch = raw_input('Enter PID in PIDxxxxx format ')
    with con.cursor() as cursor:
        try:

            mods = ((storageidtoupdate), (pidsearch))
            sql = """UPDATE `TABLE 1` SET `Storage ID`=%s  WHERE `Product ID` LIKE %s"""
            cursor.execute(sql, mods)

            print("Successfully Updated...")
        except:
            print("Oops! Something wrong")

        con.commit()
#finally:
#con.close()
