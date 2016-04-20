#!/usr/bin/python

import MySQLdb
import config   # config file has db configuration as username,password etc

database = MySQLdb.connect(config.settings['host'],config.settings['user'],\
	config.settings['password'],config.settings['database_name'] )

cursor = database.cursor()

sql = """INSERT INTO TASKS
		(Name,
         Scripts, 
         Task_set_time, 
         Task_excution_time)
         
         VALUES 
         ('Shutdown', 
         '1',
         NOW(), 
         DATE_ADD(NOW(), INTERVAL 2 HOUR))"""
try:
   cursor.execute(sql)
   database.commit()
except:
   database.rollback()
   
database.close()