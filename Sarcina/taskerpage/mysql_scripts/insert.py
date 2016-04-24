#!/usr/bin/python

import MySQLdb
import taskerpage.mysql_scripts.config as config
# config file has db configuration as username,password etc


def insert(name, address):
    """
    adds a task to tasks table
    :param name:
    :param address:
    :return: True if successful else False
    """
    database = MySQLdb.connect(config.settings['host'], config.settings['user'], \
                               config.settings['password'], config.settings['database_name'])

    cursor = database.cursor()

    sql = """INSERT INTO tasks (task_name, task_script_address) VALUES (%s, %s)"""

    try:
        cursor.execute(sql, (name, address))
        database.commit()
        database.close()
        return True

    except MySQLdb.Error as e:
        database.rollback()
        print(e.args[1])
        database.close()
        return False


