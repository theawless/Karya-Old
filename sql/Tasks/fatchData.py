#!/usr/bin/python

import MySQLdb
import config   # config file has db configuration as username,password etc

database = MySQLdb.connect(config.settings['host'],config.settings['user'],\
   config.settings['password'],config.settings['database_name'] )

cursor = database.cursor()

sql = "SELECT * FROM TASKS"
try:
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
      Name = row[1]
      Scripts = row[2]
      Set_Time = row[3]
      Execution_Time= row[4]
      print "\n Name=%s\n Scripts=%s\n Set Time=%s\n Execution Time=%s\n" % \
             (Name, Scripts, Set_Time, Execution_Time )
except:
   print "Error: unable to fecth data"

database.close()