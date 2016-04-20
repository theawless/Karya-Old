#!/usr/bin/python

import MySQLdb
import config   # config file has db configuration as username,password etc

database = MySQLdb.connect(config.settings['host'],config.settings['user'],\
   config.settings['password'],config.settings['database_name'] )

cursor = database.cursor()

sql = "UPDATE TASKS SET Task_excution_time = DATE_ADD(NOW(), INTERVAL 5 HOUR) \
                          WHERE Name = 'Shutdown'"
try:
   cursor.execute(sql)
   database.commit()
except:
   database.rollback()
   
database.close()