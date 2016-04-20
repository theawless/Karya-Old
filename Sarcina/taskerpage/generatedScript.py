import functions
def print_success():
    for i in range(8):
        functions.music("play")
        functions.open_file_in_default_application("testFile.html")
        print("I am working")
    print ("Def finished")
print_success()