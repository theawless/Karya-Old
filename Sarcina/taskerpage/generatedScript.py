import functions
def print_success():
    for i in range(5):
        functions.music("play")
        functions.open_file_in_default_application("/home/sjha/development/cs243Project/team4cs243/Tacron/testFile.html")
        print("I am working")
    print ("Def finished")
print_success()