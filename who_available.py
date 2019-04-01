import sys
import pymysql

connection = pymysql.connect(host='medicalcenter.martyhumphrey.info', port=3306, user='aardvark9', passwd='sparky12', db='Medical')
crsr = connection.cursor()

appointment_date = sys.argv[2]
appointment_time = sys.argv[1]

sql_command = "SELECT DISTINCT FirstName, Lastname FROM `nurse_sched` a INNER JOIN `nurses` b ON a.NurseID = b.ID WHERE SlotDate=('" + appointment_date + "') AND '" + appointment_time + "' BETWEEN SlotStart AND SlotEnd"

crsr.execute(sql_command)
ans = crsr.fetchall()
if crsr.rowcount == 0:
    print "The clinic is closed at that time."
else:
    full_answer = ""
    for a in ans:
        full_answer += a[0] + " " + a[1] + ", "

    print full_answer[0:len(full_answer)-2] + "are available at " + appointment_time + " on " + appointment_date + "."


