import time
import sys

class Logger(object):
	def __init__(self):
		self.terminal = sys.stdout
		self.log = open("logfile.log", "a")
		self.write("\n\n")
		self.write(time.strftime("%c"))
		self.write("\n")
	
	def write(self, message):
		self.terminal.write(message)
		self.log.write(message)  

	def flush(self):
		pass
		
sys.stdout = Logger()