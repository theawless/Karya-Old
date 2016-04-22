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
    x = datetime.now()
    targetScript = open(x+"generatedScript.py","w")

    importBlock = 'import functions' + "\n"
    repeat = 'for i in range('+str(Input["repeat"])+')'
    actions = []
    for action, parameter in Input["actions"].items():
    	if(parameter):
    		if action == "open_file":
    			actions.append('functions.open_file_in_default_application("'+Input["actions"]["open_file"]+'")')
    		elif action == "music":
    			actions.append('functions.music("'+Input["actions"]["music"]+'")')
    actions.append('print("I am working")')
    forblock = CodeBlock(repeat, actions)
    block = CodeBlock('def print_success()', [forblock, 'print ("Def finished")'])

    targetScript.write(importBlock)
    targetScript.write(block.__str__())
    targetScript.write('print_success()')

    runTime = Input.output["time_of_execution"]

os.system("python3 generatedScript.py")