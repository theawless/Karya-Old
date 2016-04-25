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

import unittest


import os, sys
SHELL_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.realpath("../"))
print(sys.path)
from lexical_analyser.textanalyser import textanalyser

from datetime import datetime


def test_text_analyser():
        dum11, dum12, result1 = textanalyser.textanalyser("Repeat 5 times after 20 hours calculate 2 + 3")
        dum21, dum22, result2 = textanalyser.textanalyser("Repeat 5 times at 10:23 pm click 100 200")
        dum31, dum32, result3 = textanalyser.textanalyser("Repeat 1 times at 8:35 am play music")
        dum41, dum42, result4 = textanalyser.textanalyser("Repeat 1 times at 12:35 pm start dictation")
        dum51, dum52, result5 = textanalyser.textanalyser("after 15 hours start dictation")
        dum61, dum62, result6 = textanalyser.textanalyser("shutdown at 8:32 pm")
        dum71, dum72, result7 = textanalyser.textanalyser("shutdown after 48 hours")
        dum81, dum82, result8 = textanalyser.textanalyser("after 20 minutes play music")
        # print(result1)
        dict1 = { 'repeat': 5,
                'time_of_execution': {'day': datetime.now().day + int((int(datetime.now().hour) + 20) / 24), 'hour': (int(datetime.now().hour) + 20) % 24, 'minute': datetime.now().minute},
                'action': {'start_dictation': '',
                'run_application': '',
                'search': '',
                'music': '',
                'shutdown': '',
                'click': {'x': '', 'y': ''},
                'type': '',
                'calculate': {'op1': 2, 'op2': 3, 'operand': '+'} }}
        dict2 = { 'repeat': 5,
                'time_of_execution': {'day': datetime.now().day, 'hour': 22, 'minute': 23},
                'action': { 'start_dictation': '',
                'run_application': '',
                'search': '',
                'music': '',
                'shutdown': '',
                'click': {'x': 100, 'y': 200},
                'type': '',
                'calculate': {'op1': '', 'op2': '', 'operand': ''}}}

        dict3 = {'repeat': 1,
                'time_of_execution': {'day': datetime.now().day, 'hour': 8, 'minute': 35},
                'action': {'start_dictation': '',
                'run_application': '',
                'search': '',
                'music': 'play',
                'shutdown': '',
                'click': {'x': '', 'y': ''},
                'type': '',
                'calculate': {'op2': '', 'op1': '', 'operand': ''}} }

        dict4 = {'repeat': 1,
                'time_of_execution': {'day': datetime.now().day+1, 'hour': 0, 'minute': 35},
                'action': {'start_dictation': '',
                'run_application': 'gedit',
                'search': '',
                'music': '',
                'shutdown': '',
                'click': {'x': '', 'y': ''},
                'type': '',
                'calculate': {'op2': '', 'op1': '', 'operand': ''}} }
        dict5 = {'repeat': '',
                'time_of_execution': {'day': datetime.now().day + int((int(datetime.now().hour) + 15) / 24), 'hour': (int(datetime.now().hour) + 15) % 24, 'minute': datetime.now().minute},
                'action': {'start_dictation': '',
                'run_application': 'gedit',
                'search': '',
                'music': '',
                'shutdown': '',
                'click': {'x': '', 'y': ''},
                'type': '',
                'calculate': {'op2': '', 'op1': '', 'operand': ''}} }
        dict6 = {'repeat': '',
                'time_of_execution': {'day': datetime.now().day , 'hour': 20, 'minute': 32},
                'action': {'start_dictation': '',
                'run_application': '',
                'search': '',
                'music': '',
                'shutdown': 'On',
                'click': {'x': '', 'y': ''},
                'type': '',
                'calculate': {'op2': '', 'op1': '', 'operand': ''}} }
        dict7 = { 'repeat': '',
                'time_of_execution': {'day': datetime.now().day + int((int(datetime.now().hour) + 48) / 24), 'hour': (int(datetime.now().hour) + 48) % 24, 'minute': datetime.now().minute},
                'action': {'start_dictation': '',
                'run_application': '',
                'search': '',
                'music': '',
                'shutdown': 'On',
                'click': {'x': '', 'y': ''},
                'type': '',
                'calculate': {'op1': '', 'op2': '', 'operand': ''} }}
        dict8 = { 'repeat': '',
                'time_of_execution': {'day': datetime.now().day + int((datetime.now().hour + int((datetime.now().minute + 20) / 60))/ 24), 'hour': int(datetime.now().hour + int((datetime.now().minute + 20) / 60))%24, 'minute': (int(datetime.now().minute) + 20) % 60},

                'action': {'start_dictation': '',
                'run_application': '',
                'search': '',
                'music': 'play',
                'shutdown': '',
                'click': {'x': '', 'y': ''},
                'type': '',
                'calculate': {'op2': '', 'op1': '', 'operand': ''}}}


        #for k in diffkeys:
        #   print (k, ':', result4[k], '->', dict4[k])
        # print(len(diffkeys))
        # if (len(diffkeys)==0):
        #   print("ok")
        diffkeys = [k for k in result1 if result1[k] != dict1[k]]
        a1=len(diffkeys)
        diffkeys = [k for k in result2 if result2[k] != dict2[k]]
        a2=len(diffkeys)
        diffkeys = [k for k in result3 if result3[k] != dict3[k]]
        a3=len(diffkeys)
        diffkeys = [k for k in result4 if result4[k] != dict4[k]]
        a4=len(diffkeys)
        diffkeys = [k for k in result5 if result5[k] != dict5[k]]
        a5=len(diffkeys)
        diffkeys = [k for k in result6 if result6[k] != dict6[k]]
        a6=len(diffkeys)
        diffkeys = [k for k in result7 if result7[k] != dict7[k]]
        a7=len(diffkeys)
        diffkeys = [k for k in result8 if result8[k] != dict8[k]]
        a8=len(diffkeys)
        if a1 == 0 and a2 == 0 and a3 == 0 and a4 == 0 and a5 == 0 and a6 == 0 and a7 == 0 and a8 == 0 :
            print("ok")