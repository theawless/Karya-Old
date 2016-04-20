
import MySQLdb
import config   # config file has db configuration as username,password etc

database = MySQLdb.connect(config.settings['host'],config.settings['user'],config.settings['password']\
	,config.settings['database_name'] )

cursor = database.cursor()

sql = "CREATE DATABASE IF NOT EXISTS TESTDB"

cursor.execute(sql)

print("No error and warning means that query exceuted successfully.")
