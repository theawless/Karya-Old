"""Sets up the logger."""
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

import logging
import os

logger = logging.getLogger('sarcina')
SARCINA_PATH = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(SARCINA_PATH + '/.logs'):
    os.makedirs(SARCINA_PATH + '/.logs')

LOG_DIR_PATH = SARCINA_PATH + "/.logs/"


def _setup_logger():
    # setting format of log
    formatter = logging.Formatter('%(threadName)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.DEBUG)
    # file location
    debug_log = LOG_DIR_PATH + 'log.txt'

    # adding handler for console logs
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    # adding handler for file logs
    fh = logging.FileHandler(debug_log)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.debug('Setlog logger setup done')


_setup_logger()
