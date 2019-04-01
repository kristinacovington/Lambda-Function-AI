import sys
import pymysql

connection = pymysql.connect(host='medicalcenter.martyhumphrey.info', port=3306, user='aardvark9', passwd='sparky12', db='Medical')
crsr = connection.cursor()

first_name = sys.argv[1]

sql_command = "SELECT DISTINCT Lastname FROM `nurses` WHERE FirstName='" + first_name + "'"
                

crsr.execute(sql_command)
ans = crsr.fetchone()
if crsr.rowcount == 0:
    print "I am not aware of that person."
else:
    print "The last name of " + first_name + " is " + ans[0] + "."
