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

# !/usr/bin/python
# import testData as Input

import os
from datetime import datetime
from threading import Timer


class CodeBlock():
    """
    Class to generate script
    """

    def __init__(self, head, block):
        """
        Initializing CodeBlock class
        :param head: Head part for python code e.g if a > b for if condition, def helloWorld() for functions ..etc
        :param block: Block part for python code e.g print("hello world") inside a loop
        :return: null
        """
        self.head = head
        self.block = block
        self.Input = {}
        self.name = ""

    def __str__(self, indent=""):
        """
        Converts CodeBlock code to string
        :param indent:
        :return: python code string
        """
        result = indent + self.head + ":\n"
        indent += "    "
        for block in self.block:
            if isinstance(block, CodeBlock):
                result += block.__str__(indent)
            else:
                result += indent + block + "\n"
        return result


class Script():
    """
    Script generating class
    """

    def __init__(self):
        """
        Initializes variable
        :return: null
        """
        self.Input = {}
        self.name = ""

    def writeScript(self, Input):
        """
        Generates python code and write to a python file
        :param Input: The dictionary passed by lexical analyser
        :return: Name of the python file created
        """
        self.Input = Input
        print("I am here")
        x = datetime.now()
        print(x)
        x = str(x).replace(" ", "_")
        x = str(x).replace(".", "_")
        x = str(x).replace(":", "_")
        self.name = str(x) + "generatedScript.py"
        targetScript = open(self.name, "w")

        importBlock = 'import sarcina.taskerpage.functions as functions' + "\n"
        repeat = 'for i in range(' + str(Input["repeat"]) + ')'
        actions = []
        for action, parameter in Input["action"].items():
            if (parameter):
                if action == "run_application":
                    actions.append('functions.open_application("' + Input["action"]["run_application"] + '")')
                elif action == "music":
                    actions.append('functions.music("' + Input["action"]["music"] + '")')
                elif action == "click":
                    if Input["action"]["click"]["x"] and Input["action"]["click"]["y"]:
                        actions.append('functions.click("' + str(Input["action"]["click"]["x"]) + ", " + str(
                            Input["action"]["click"]["y"]) + '")')
                elif action == "shutdown":
                    actions.append('functions.shutdown("' + (Input["action"]["shutdown"]) + '")')

        actions.append('print("I am working")')
        print(actions)
        forblock = CodeBlock(repeat, actions)
        block = CodeBlock('def print_success()', [forblock, 'print ("Def finished")'])

        targetScript.write(importBlock)
        targetScript.write(block.__str__())
        targetScript.close()
        return self.name

    def set_written_script(self):
        """
        Sets generated python script for execution at some time
        :return: name of the python file set for execution
        """
        m = __import__(self.name.split('.')[0])
        # from na
        # me.split('.')[0] import print_success
        # taskScheduler.setTask(Input["time_of_execution"]["day"], Input["time_of_execution"]["hour"],
        #                      Input["time_of_execution"]["minute"]
        #                      )
        x = datetime.today()
        day = self.Input["time_of_execution"]["day"]
        minute = self.Input["time_of_execution"]["minute"]
        hour = self.Input["time_of_execution"]["hour"]
        y = x.replace(day=day, hour=hour, minute=minute, second=0, microsecond=0)
        delta_t = y - x
        secs = delta_t.seconds + 1
        t = Timer(secs, m.print_success)
        t.start()
        return self.name
        # os.system("python3 generatedScript.py")
