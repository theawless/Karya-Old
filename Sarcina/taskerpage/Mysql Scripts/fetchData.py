#!/usr/bin/python

import MySQLdb
import config   # config file has db configuration as username,password etc

def fetchData():
   output = []
   database = MySQLdb.connect(config.settings['host'],config.settings['user'],\
      config.settings['password'],config.settings['database_name'] )

   cursor = database.cursor()

   sql = "SELECT * FROM SCRIPTS"
   try:
      cursor.execute(sql)
      results = cursor.fetchall()
      for row in results:
         tempObject = {}
         tempObject["index"] = row[0]
         tempObject["name"] = row[1]
         tempObject["code"] = row[2]
         tempObject["file_location"] = row[3]
         tempObject["applications_involved"] = row[4]
         tempObject["need_sudo_permission"] = row[5]
         output.append(tempObject)

   except MySQLdb.Error as e:
      print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))

   database.close()
   return output