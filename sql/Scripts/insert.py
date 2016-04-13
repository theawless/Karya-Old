#!/usr/bin/python

import MySQLdb
import config   # config file has db configuration as username,password etc

database = MySQLdb.connect(config.settings['host'],config.settings['user'],\
	config.settings['password'],config.settings['database_name'] )

cursor = database.cursor()

sql = """INSERT INTO SCRIPTS
		(Name,
         file_location,
         script_code, 
         Applications_involved, 
         Need_Sudo_Permission)
         
         VALUES 
         ('Shutdown', 
         '/home/sjha/development/cs243Project/team4cs243/scripts/shutdown',
         'print("Hello world")',
         'System', 
         1)"""
try:
   cursor.execute(sql)
   database.commit()
except:
   database.rollback()
   
database.close()