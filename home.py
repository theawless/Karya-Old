import os, sys, subprocess
import gi
import urllib.parse
import urllib.request
import json
#from gui_functions import search, local_search, exec_task
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, WebKit


class EntryWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Entry Demo")
        self.set_size_request(200, 100)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        Entry01 = Gtk.Entry()
        Entry01.set_text("Write something..")
        vbox.pack_start(Entry01, True, True, 0)
#        url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyB0lhXv_RqGJRQnlQ5ZrihDLy3TBrEmjIk%20&cx=017576662512468239146:omuauf_lfve&q="
        url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyDKXPuaXh84T_tVVQcxQdbQS8TzNk2uuuU%20&cx=017576662512468239146:omuauf_lfve&q="
#        view = WebKit.WebView()

#        view.open(url)
#        vbox.pack_start(view, True, True, 0)

        button01 = Gtk.Button.new_with_label("Search on web")
        button01.connect("clicked", self.search, url, Entry01, vbox)
        vbox.pack_start(button01, True, True, 0)

        button02 = Gtk.Button.new_with_label("Search locally")
        button02.connect("clicked", self.search_local, vbox, Entry01)
        vbox.pack_start(button02, True, True, 0)

        button03 = Gtk.Button.new_with_label("Execute task")
        button03.connect("clicked", self.exec_task, vbox, Entry01)
        vbox.pack_start(button03, True, True, 0)

    def search(self, button, url, Entry01, vbox):
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

    def search_local(self, button, vbox, Entry01):
        search_keywords = Entry01.get_text()
        print("Searching in local files...")
        for root, dirs, files in os.walk('../../../'):
            for file in files:
                if search_keywords in file:
                    print(file)
#        button03 = Gtk.Button.new_with_label("test successfull")
#        vbox.pack_start(button03, True, True, 0)
    
    def exec_task(self, button, vbox, Entry01):
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
            #print(command[5:])
            subprocess.call(["xdg-open", command[5:]])
            os.system(command[5:])
            
#else
        else:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING,Gtk.ButtonsType.OK_CANCEL, "Command Not Found")
            dialog.format_secondary_text("Enter a valid command")
            response = dialog.run()
            if response == (Gtk.ResponseType.OK or Gtk.ResponseType.CANCEL):
                dialog.destroy()
                






win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()




