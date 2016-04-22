#!/usr/bin/python

import MySQLdb
import config   # config file has db configuration as username,password etc

database = MySQLdb.connect(config.settings['host'],config.settings['user'],config.settings['password']\
	,config.settings['database_name'] )

cursor = database.cursor()

sql = "SELECT VERSION()"

cursor.execute(sql)

result = cursor.fetchone()

print "MySql Database version is : %s " % result

database.close()