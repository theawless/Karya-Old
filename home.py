import os, sys, subprocess
import gi
import urllib.parse
import urllib.request
import json
from text_analyser import text_analyser
from functions import localsearch

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, WebKit


class EntryWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Tasker")
        self.set_size_request(200, 100)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        Entry01 = Gtk.Entry()
        Entry01.set_text("Write something..")
        vbox.pack_start(Entry01, True, True, 0)
        # url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyB0lhXv_RqGJRQnlQ5ZrihDLy3TBrEmjIk%20&cx=017576662512468239146:omuauf_lfve&q="
        url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyDKXPuaXh84T_tVVQcxQdbQS8TzNk2uuuU%20&cx=017576662512468239146:omuauf_lfve&q="
        # view = WebKit.WebView()
        # view.open(url)
        # vbox.pack_start(view, True, True, 0)

        button_search_on_web = Gtk.Button.new_with_label("Search on web")
        button_search_on_web.connect("clicked", self.search, url, Entry01, vbox)
        vbox.pack_start(button_search_on_web, True, True, 0)

        button_search_locally = Gtk.Button.new_with_label("Search locally")
        button_search_locally.connect("clicked", self.search_local, vbox, Entry01)
        vbox.pack_start(button_search_locally, True, True, 0)

        button_execute = Gtk.Button.new_with_label("Execute")
        button_execute.connect("clicked", self.exec_task, vbox, Entry01)
        vbox.pack_start(button_execute, True, True, 0)


    def search(self, button, url, Entry01, vbox):
        print("\"Search\" button was clicked")
        line_to_search = Entry01.get_text()
        words_to_search = line_to_search.split()
        search_keywords = ""
        for word in words_to_search:
            search_keywords += word + '+'
        url = url + search_keywords
        print("URL is : " + url)
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
        button = [0] * 1000
        i = 0
        search_result_filepaths, search_result_filenames = localsearch(search_keywords)
        for res in search_result_filepaths:
            button[i] = Gtk.Button.new_with_label(search_result_filenames[i])
            button[i].connect("clicked", self.open_file_shown_in_search_result, search_result_filepaths[i])
            vbox.pack_start(button[i], True, True, 0)
            button[i].show()
            i += 1


    def open_file_shown_in_search_result(self, button, filepathh):
        subprocess.call(["xdg-open", filepathh])



    def exec_task(self, button, vbox, Entry01):
        command = Entry01.get_text()
        xx = text_analyser(command)


        # Shutdown now
        # if command == "shutdown now":
        #     os.system("sudo shutdown 0")
        # else:
        #     dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK_CANCEL, "Command Not Found")
        #     dialog.format_secondary_text("Enter a valid command")
        #     response = dialog.run()
        #     if response == (Gtk.ResponseType.OK or Gtk.ResponseType.CANCEL):
        #         dialog.destroy()


win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
