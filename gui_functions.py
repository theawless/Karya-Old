EntryWindow_instance = EntryWindow()

def search(EntryWindow_instance, button, url, Entry01, vbox):
    print("\"Search\" button was clicked")
    search_keywords = Entry01.get_text()
    url = url + search_keywords
    print("URL is : "+url)
    response = urllib.request.urlopen(url)
    content = response.read()
    data = json.loads(content.decode("utf8"))
    for i in data['items']:
        print(i['title'])
        print(i['link'])
        print(i['snippet'])

def search_local(EntryWindow_instance, button, vbox, Entry01):
    search_keywords = Entry01.get_text()
    print("Searching in local files...")
    for root, dirs, files in os.walk('../../../'):
        for file in files:
            if search_keywords in file:
                print(file)
#        button03 = Gtk.Button.new_with_label("test successfull")
#        vbox.pack_start(button03, True, True, 0)

def exec_task(EntryWindow_instance, button, vbox, Entry01):
    command = Entry01.get_text()
#Shutdown now
    if command=="shutdown now":
        os.system("sudo shutdown 0")
#Reboot
    elif command==("reboot" or "restart"):
        os.system("sudo shutdown 2 -r")
#shutdown in x minutes
    elif command[0]=='s'and command[1]=='h'and command[2]=='u'and command[3]=='t'and command[4]=='d'and command[5]=='o'and command[6]=='w'and command[7]=='n':
        os.system("sudo shutdown "+command[12])
#Open Applications or files
    elif  command[0]==('o' or 'O') and command[1]=='p' and command[2]=='e' and command[3]=='n':
        print(command[5:])
        #subprocess.call(["xdg-open", command[5])
        
#else
    else:
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,Gtk.ButtonsType.OK_CANCEL, "Command Not Found")
        dialog.format_secondary_text("Enter a valid command")
        response = dialog.run()
        if response == (Gtk.ResponseType.OK or Gtk.ResponseType.CANCEL):
            dialog.destroy()
            



