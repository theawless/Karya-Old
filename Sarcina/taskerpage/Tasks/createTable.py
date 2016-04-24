#!/usr/bin/python

import MySQLdb
import config   # config file has db configuration as username,password etc

database = MySQLdb.connect(config.settings['host'],config.settings['user'],\
	config.settings['password'],config.settings['database_name'] )

cursor = database.cursor()

sql = """CREATE TABLE IF NOT EXISTS TASKS (
		 Id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
		 Name varchar(255),
         Scripts  varchar(255) NOT NULL, 
         Task_set_time TIMESTAMP,
         Task_excution_time TIMESTAMP
 		)"""

cursor.execute(sql)

database.close()