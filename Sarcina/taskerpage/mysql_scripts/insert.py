#!/usr/bin/python

import MySQLdb
import taskerpage.mysql_scripts.config as config
# config file has db configuration as username,password etc


def insert(name, address):
    database = MySQLdb.connect(config.settings['host'], config.settings['user'], \
                               config.settings['password'], config.settings['database_name'])

    cursor = database.cursor()

    sql = """INSERT INTO tasks (task_name, task_script_address) VALUES (%s, %s)"""

    try:
        cursor.execute(sql, (name, address))
        database.commit()
    except MySQLdb.Error as e:
        database.rollback()
        print(e.args[1])

    database.close()
