#!/usr/bin/python

import MySQLdb
import config   # config file has db configuration as username,password etc

database = MySQLdb.connect(config.settings['host'],config.settings['user'],\
	config.settings['password'],config.settings['database_name'] )

cursor = database.cursor()

sql = """CREATE TABLE  IF NOT EXISTS SCRIPTS (
		 Id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
         Name  varchar(255) NOT NULL,
         file_location  varchar(255),
         script_code text,
         Applications_involved varchar(500),  
         Need_Sudo_Permission int
 		)"""

cursor.execute(sql)

database.close()