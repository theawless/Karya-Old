#!/usr/bin/python

import MySQLdb
import config

# Open database connection

db = MySQLdb.connect(config.settings['host'],config.settings['user'],config.settings['password']\
	,config.settings['db_name'] )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 \
                          WHERE SEX = '%c'" % ('M')
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()