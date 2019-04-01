import sys
import pymysql

connection = pymysql.connect(host='medicalcenter.martyhumphrey.info', port=3306, user='aardvark9', passwd='sparky12', db='Medical')
crsr = connection.cursor()

appointment_date = sys.argv[3]

first_name = sys.argv[1]
last_name = sys.argv[2]

sql_command = "SELECT DISTINCT SlotStart, SlotEnd FROM `nurse_sched` a INNER JOIN `nurses` b ON a.NurseID = b.ID WHERE SlotDate=DATE('" + appointment_date + "') AND FirstName='" + first_name + "' AND Lastname='" + last_name + "'"

crsr.execute(sql_command)
ans = crsr.fetchone()
if crsr.rowcount == 0:
    print "I am not aware of that person."
else:
    print first_name + " " + last_name + " is available between %s and %s." % (ans[0], ans[1])
