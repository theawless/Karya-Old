from datetime import datetime
from threading import Timer
import generatedScript

x=datetime.today()
y=x.replace(day=x.day, hour=19, minute=10, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

t = Timer(secs, generatedScript.print_success)
t.start()