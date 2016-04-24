import unittest
import textanalyser
from datetime import datetime



result1 = textanalyser.textanalyser("Repeat 5 times after 20 hours calculate 2 + 3")
result2 = textanalyser.textanalyser("Repeat 1 times at 10:23 pm calculate 10 - 7")
result3 = textanalyser.textanalyser("Repeat 1 times at 8:35 am play music")
result4 = textanalyser.textanalyser("Repeat 1 times at 12:35 pm start dictation")
#print(result4)
dict1 = { 'repeat': 5, 
		'time_of_execution': {'day': datetime.now().day + int((int(datetime.now().hour) + 20) / 24), 'hour': (int(datetime.now().hour) + 20) % 24, 'minute': datetime.now().minute}, 
		'action': {'start_dictation': '', 
		'run_application': '',
		'search': '',  
		'play': '',
		'click': {'x': '', 'y': ''},
		'calculate': {'op1': 2, 'op2': 3, 'operand': '+'} }}
dict2 = { 'repeat': 1,
		'time_of_execution': {'day': datetime.now().day, 'hour': 22, 'minute': 23},
		'action': { 'start_dictation': '',
		'run_application': '',
		'search': '', 
		'play': '',
		'click': {'x': '', 'y': ''},
		'calculate': {'op1': 10, 'op2': 7, 'operand': '-'}}}

dict3 = {'repeat': 1,
		'time_of_execution': {'day': datetime.now().day, 'hour': 8, 'minute': 35},
		'action': {'start_dictation': '', 
		'run_application': '', 
		'search': '', 
		'play': ' music',
		'click': {'x': '', 'y': ''},
		'calculate': {'op2': '', 'op1': '', 'operand': ''}} }

dict4 = {'repeat': 1,
		'time_of_execution': {'day': datetime.now().day+1, 'hour': 0, 'minute': 35},
		'action': {'start_dictation': '', 
		'run_application': 'gedit', 
		'search': '', 
		'play': '',
		'click': {'x': '', 'y': ''},
		'calculate': {'op2': '', 'op1': '', 'operand': ''}} }
		
diffkeys = [k for k in result1 if result1[k] != dict1[k]]
#for k in diffkeys:
#	print (k, ':', result4[k], '->', dict4[k])
a = (len(diffkeys))
print(len(diffkeys))

if (a==0):
	print("ok")