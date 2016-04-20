import os
import sys
import re
import subprocess


class TextAnalyser:
    def __init__(self,input_text):
        # Open an application or file
        if input_text.startswith("open" or "Open"):
            subprocess.call(["xdg-open", input_text[5:]])
            os.system(input_text[5:])

        # Shutdown
        elif "shutdown" in input_text:
            if input_text == "shutdown now":
                os.system("sudo shutdown 0")
            elif "shutdown in" or "shutdown after" in input_text :
                minutes = [int(s) for s in input_text.split() if s.isdigit()]
                os.system("sudo shutdown " + minutes[0])

        # Reboot
        elif "restart" or "reboot" in input_text:
            if input_text == "restart now":
                os.system("sudo shutdown -r 0")
            elif "restart in" or "restart after" in input_text :
                minutes = [int(s) for s in input_text.split() if s.isdigit()]
                os.system("sudo shutdown -r " + minutes[0])

        # elif input_text.startswith("rename"):
        #     s = input_text.split()
        #     name_of_file_to_rename = s[1]
