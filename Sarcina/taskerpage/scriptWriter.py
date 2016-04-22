#!/usr/bin/python
# import testData as Input
import os
from datetime import datetime

class CodeBlock():
    def __init__(self, head, block):
        self.head = head
        self.block = block
    def __str__(self, indent=""):
        result = indent + self.head + ":\n"
        indent += "    "
        for block in self.block:
            if isinstance(block, CodeBlock):
                result += block.__str__(indent)
            else:
                result += indent + block + "\n"
        return result

def writeScript(Input):
    print("I am here")
    x = datetime.now()
    name = "generatedScript.py"
    targetScript = open(name,"w")

    importBlock = 'import functions' + "\n"
    repeat = 'for i in range('+str(Input["repeat"])+')'
    actions = []
    for action, parameter in Input["action"].items():
    	if(parameter):
            if action == "run_application":
                actions.append('functions.open_application("'+Input["action"]["run_application"]+'")')
            elif action == "play":
                actions.append('functions.music("'+Input["action"]["play"]+'")')
            

    actions.append('print("I am working")')
    print(actions)
    forblock = CodeBlock(repeat, actions)
    block = CodeBlock('def print_success()', [forblock, 'print ("Def finished")'])

    targetScript.write(importBlock)
    targetScript.write(block.__str__())
    targetScript.write('print_success()')
    targetScript.close()

    import taskScheduler
    taskScheduler.setTask(Input["time_of_execution"]["day"],Input["time_of_execution"]["hour"],Input["time_of_execution"]["minute"]
        )

# os.system("python3 generatedScript.py")