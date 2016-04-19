"""Sets up the logger."""

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
