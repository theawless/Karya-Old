import os
import sys
import re
import subprocess
from datetime import datetime

def tryInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def textanalyser(text):
    inputText = text.lower()
    output = { "repeat" : "",
               "time_of_execution": {
                    "day" : "",
                    "hour" : "",
                    "minute" : ""
               },
               "action" : { "start_dictation" : "",
                            "run_application" : "",
                            "search" : "",
                            "play" : "",
                            "calculate" : {
                                "op1" : "",
                                "op2" : "",
                                "operand" : ""
                                }
                        }
             }
    state = 0

    list_of_words = inputText.split()

    if "repeat" in list_of_words:
        times = list_of_words[list_of_words.index("repeat")+1]
        if tryInt(times):
            output["repeat"] = int(times)

    if "start dictation" in inputText or "dictate" in inputText:
        output["action"]["run_application"] = "gedit"

    if "run" in list_of_words:
        application_to_open = list_of_words[list_of_words.index("run")+1]
        output["action"]["run_application"] = application_to_open

    if "search" in list_of_words:
        to_search = " ".join(inputText.split("search",1)[1:])
        output["action"]["search"] = to_search

    if "play" in list_of_words:
        output["action"]["play"] = " ".join(inputText.split("play",1)[1:])

    if "calculate" in list_of_words:
        op1 = list_of_words[list_of_words["calculate"]+1]
        op2 = list_of_words[list_of_words["calculate"]+3]
        operand = list_of_words[list_of_words["calculate"]+2]

        if(tryInt(op1)):
            output["action"]["calculate"]["op1"] = int(op1)
        if(tryInt(op2)):
            output["action"]["calculate"]["op2"] = int(op2)

        if(operand == "+"):
            output["action"]["calculate"]["operand"] = "+"
        elif(operand == "-"):
            output["action"]["calculate"]["operand"] = "-"
        elif(operand == "*"):
            output["action"]["calculate"]["operand"] = "*"
        elif(operand == "/"):
            output["action"]["calculate"]["operand"] = "/"
       
    if "at" in list_of_words:
        state = 1
        time = list_of_words[list_of_words.index("at")+1]
        amOrPm = list_of_words[list_of_words.index("at")+2]

        if("pm" in amOrPm):
            output["time_of_execution"]["day"] = 0
            if(tryInt(time.split(":")[0])):
                output["time_of_execution"]["hour"] = int(time.split(":")[0]) + 12

            if(tryInt(time.split(":")[1])):
                output["time_of_execution"]["minute"] = int(time.split(":")[1])

        else:
            output["time_of_execution"]["day"] = 0
            if(tryInt(time.split(":")[0])):
                output["time_of_execution"]["hour"] = int(time.split(":")[0])

            if(tryInt(time.split(":")[1])):
                output["time_of_execution"]["minute"] = int(time.split(":")[1])


    if "after" in list_of_words:
        state = 1

        duration = list_of_words[list_of_words.index("after")+1]
        if(tryInt(duration)):
            factor = list_of_words[list_of_words.index("after")+2]
            if(factor == "minute" or factor == "minutes"):
                output["time_of_execution"]["day"] = 0
                tempMinute = int(datetime.now().minute) + int(duration)
                output["time_of_execution"]["minute"] = tempMinute % 60
                output["time_of_execution"]["hour"] = int(tempMinute / 60)
            
            elif(factor == "hour" or factor == "hours"):
                tempHour = int(datetime.now().hour) + int(duration)
                output["time_of_execution"]["minute"] = datetime.now().minute
                output["time_of_execution"]["hour"] = tempHour % 24
                output["time_of_execution"]["day"] = datetime.now().day + int(tempHour / 24) 

    if state == "0":
        pass

    if state == "1":
        pass
    
    return output

output = textanalyser("Repeat 5 times after 20 hours run firefox play audio search kutta ka bachha")
print(output)