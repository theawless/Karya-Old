from datetime import datetime
from threading import Timer

import sys

sys.path.insert(0, '/home/sjha/development/cs243Project/team4cs243/Sarcina/lexical_analyser/')
import generatedScript


def setTask(day, hour, minute):
    x = datetime.today()
    y = x.replace(day=day, hour=hour, minute=minute, second=0, microsecond=0)
    delta_t = y - x

    secs = delta_t.seconds + 1

    t = Timer(secs, generatedScript.print_success)
    t.start()


#useless