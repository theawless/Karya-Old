from gi.overrides import Gtk

import functions
from Sarcina.homepage.search import Search

def zeroStateTasker(Input):
    if Input["repeat"]:
        repeat = int(Input["repeat"])

    else:
        repeat = 1

    for i in range(repeat):
        for action, parameter in Input["action"].items():
            if parameter:
                if action == "start_dictation":
                    functions.open_application("gedit")
                elif action == "run_application":
                    functions.open_application(parameter)
                elif action == "search":
                    S = Search(parameter)
                    S.show(Gtk.Builder())
                elif action == "music":
                    functions.music(parameter)
                elif action == "shutdown":
                    functions.shutdown()
                elif action == "click":
                    if parameter["x"] and parameter["y"]:
                        functions.click(parameter["x"],parameter["y"])
                elif action == "calculate":
                    if parameter["op1"] and parameter["op2"] and parameter["operand"]:
                        result = functions.calculate(parameter["op1"],parameter["op2"],parameter["operand"])