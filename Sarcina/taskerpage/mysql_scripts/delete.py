#!/usr/bin/python

import MySQLdb
import taskerpage.mysql_scripts.config as config


def delete(index):
    database = MySQLdb.connect(config.settings['host'], config.settings['user'], \
                               config.settings['password'], config.settings['database_name'])

    print(index)
    cursor = database.cursor()

    sql = "DELETE FROM `SCRIPTS` WHERE `Id` = %s"
    try:
        cursor.execute(sql, (int(index),))
        database.commit()
    except MySQLdb.Error as e:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        database.rollback()

    database.close()
