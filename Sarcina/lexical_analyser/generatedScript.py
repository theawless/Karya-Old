import functions

def print_success():
    for i in range(3):
        functions.open_application("firefox")
        print("I am working")
    print ("Def finished")