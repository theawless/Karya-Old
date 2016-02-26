#!/usr/bin/python

import MySQLdb
import config   # config file has db configuration as username,password etc

database = MySQLdb.connect(config.settings['host'],config.settings['user'],\
   config.settings['password'],config.settings['database_name'] )

cursor = database.cursor()

sql = "SELECT * FROM SCRIPTS"
try:
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
      Name = row[1]
      file_location = row[2]
      Applications_involved = row[3]
      Need_Sudo_Permission = row[4]
      print "\n Name=%s\n file_location=%s\n Applications_involved=%s\n Need_Sudo_Permission=%d\n" % \
             (Name, file_location, Applications_involved, Need_Sudo_Permission )
except:
   print "Error: unable to fecth data"

database.close()