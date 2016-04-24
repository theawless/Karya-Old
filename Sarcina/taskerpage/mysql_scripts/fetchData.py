#!/usr/bin/python

import MySQLdb
import taskerpage.mysql_scripts.config as config

# config file has db configuration as username,password etc


def fetchData():
    """
    Returns all tasks, previously set by user from tasks table
    :return: task object array
    """
    output = []
    database = MySQLdb.connect(config.settings['host'], config.settings['user'], \
                               config.settings['password'], config.settings['database_name'])

    cursor = database.cursor()

    sql = "SELECT * FROM tasks"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            tempObject = {}
            tempObject["task_id"] = row[0]
            tempObject["name"] = row[1]
            tempObject["file_location"] = row[2]
            output.append(tempObject)

    except MySQLdb.Error as e:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))

    database.close()
    return output
