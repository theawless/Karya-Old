#!/usr/bin/python

import MySQLdb
import taskerpage.mysql_scripts.config as config


def delete(index):
    """
    delets script corresponding to index from scripts table
    :param index:
    :return: True if successful else False
    """
    database = MySQLdb.connect(config.settings['host'], config.settings['user'], \
                               config.settings['password'], config.settings['database_name'])

    print(index)
    cursor = database.cursor()

    sql = "DELETE FROM `SCRIPTS` WHERE `Id` = %s"
    try:
        cursor.execute(sql, (int(index),))
        database.commit()
        database.close()
        return True

    except MySQLdb.Error as e:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        database.rollback()
        database.close()
        return False