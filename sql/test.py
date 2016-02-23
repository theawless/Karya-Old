#!/usr/bin/python

import MySQLdb
import config

db = MySQLdb.connect(config.settings['host'],config.settings['user'],config.settings['password']\
	,config.settings['db_name'] )

cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
db.close()