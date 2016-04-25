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
