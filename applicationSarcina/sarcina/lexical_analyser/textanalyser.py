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

import os
import sys
import re
import subprocess
from datetime import datetime

sys.path.insert(0, '/home/harshit/Desktop/working/Sarcina/taskerpage/')
from sarcina.taskerpage.scriptWriter import Script


def tryInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def textanalyser(text):
    inputText = text.lower()
    output = {"repeat": "",
              "time_of_execution": {
                  "day": "",
                  "hour": "",
                  "minute": ""
              },
              "action": {"start_dictation": "",
                         "run_application": "",
                         "search": "",
                         "play": "",
                         "shutdown": "",
                         "click": {
                             "x": "",
                             "y": ""
                         },
                         "calculate": {
                             "op1": "",
                             "op2": "",
                             "operand": ""
                         }
                         }
              }
    state = 0

    list_of_words = inputText.split()

    if "repeat" in list_of_words:
        times = list_of_words[list_of_words.index("repeat") + 1]
        if tryInt(times):
            output["repeat"] = int(times)

    if "start dictation" in inputText or "dictate" in inputText:
        output["action"]["run_application"] = "gedit"

    if "shutdown" in inputText:
        output["action"]["shutdown"] = "On"

    if "run" in list_of_words:
        application_to_open = list_of_words[list_of_words.index("run") + 1]
        output["action"]["run_application"] = application_to_open

    if "search" in list_of_words:
        to_search = " ".join(inputText.split("search", 1)[1:])
        output["action"]["search"] = to_search

    if "play" in list_of_words:
        output["action"]["play"] = " ".join(inputText.split("play", 1)[1:])

    # if "calculate" in list_of_words:
    #     op1 = list_of_words[list_of_words.index["calculate"] + 1]
    #     op2 = list_of_words[list_of_words.index["calculate"] + 3]
    #     operand = list_of_words[list_of_words.index["calculate"] + 2]

    #     if tryInt(op1):
    #         output["action"]["calculate"]["op1"] = int(op1)
    #     if tryInt(op2):
    #         output["action"]["calculate"]["op2"] = int(op2)

    #     if operand == "+":
    #         output["action"]["calculate"]["operand"] = "+"
    #     elif operand == "-":
    #         output["action"]["calculate"]["operand"] = "-"
    #     elif operand == "*":
    #         output["action"]["calculate"]["operand"] = "*"
    #     elif operand == "/":
    #         output["action"]["calculate"]["operand"] = "/"

    if "click" in list_of_words:
        pos1 = list_of_words[list_of_words.index("click") + 1]
        pos2 = list_of_words[list_of_words.index("click") + 2]
        if tryInt(pos1):
            output["action"]["click"]["x"] = int(pos1)

        if tryInt(pos2):
            output["action"]["click"]["y"] = int(pos2)

        if pos1 == "top":
            output["action"]["click"]["y"] = 1360

        if pos2 == "bottom":
            output["action"]["click"]["x"] = 755

    if "at" in list_of_words:
        state = 1
        time = list_of_words[list_of_words.index("at") + 1]
        amOrPm = list_of_words[list_of_words.index("at") + 2]

        if "pm" in amOrPm:
            if int(time.split(":")[0]) == 12:
                output["time_of_execution"]["day"] = datetime.now().day + 1
                output["time_of_execution"]["hour"] = 0
                output["time_of_execution"]["minute"] = int(time.split(":")[1])
            else:
                output["time_of_execution"]["day"] = datetime.now().day
                if tryInt(time.split(":")[0]):
                    output["time_of_execution"]["hour"] = int(time.split(":")[0]) + 12

                if tryInt(time.split(":")[1]):
                    output["time_of_execution"]["minute"] = int(time.split(":")[1])

        else:
            output["time_of_execution"]["day"] = datetime.now().day
            if tryInt(time.split(":")[0]):
                output["time_of_execution"]["hour"] = int(time.split(":")[0])

            if tryInt(time.split(":")[1]):
                output["time_of_execution"]["minute"] = int(time.split(":")[1])

    if "after" in list_of_words:
        state = 1
        duration = list_of_words[list_of_words.index("after") + 1]
        if tryInt(duration):
            factor = list_of_words[list_of_words.index("after") + 2]
            if factor == "minute" or factor == "minutes":
                output["time_of_execution"]["day"] = datetime.now().day
                tempMinute = int(datetime.now().minute) + int(duration)
                output["time_of_execution"]["minute"] = tempMinute % 60
                output["time_of_execution"]["hour"] = datetime.now().hour + int(tempMinute / 60)

            elif factor == "hour" or factor == "hours":
                tempHour = int(datetime.now().hour) + int(duration)
                output["time_of_execution"]["minute"] = datetime.now().minute
                output["time_of_execution"]["hour"] = tempHour % 24
                output["time_of_execution"]["day"] = datetime.now().day + int(tempHour / 24)

    if state == 0:
        pass

    if state == 1:
        # write script and sets task
        script = Script()
        name_of_script = script.writeScript(output)

    return name_of_script, script, output

# output = textanalyser("Repeat 3 times after 2 minute run firefox")
# print(output)
