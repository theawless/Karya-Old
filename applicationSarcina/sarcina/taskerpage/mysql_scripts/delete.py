# Sarcina - A voice based tasker/assistant for Ubuntu.
# Copyright (C) <2016>  <Abhinav Singh>
# Copyright (C) <2016>  <Abhinav Prince>
# Copyright (C) <2016>  <Harshit Rai>
# Copyright (C) <2016>  <Suraj Jha>
#
# This file is part of Sarcina.
#
# Sarcina is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Sarcina is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Sarcina.  If not, see <http://www.gnu.org/licenses/>.

# !/usr/bin/python

import MySQLdb
from sarcina.taskerpage.mysql_scripts import config


def delete(index):
    """
    delets script corresponding to index from scripts table
    :param index:
    :return: True if successful else False
    """
    database = MySQLdb.connect(config.settings['host'], config.settings['user'],
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
