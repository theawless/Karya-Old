import os, sys, subprocess
import gi
import urllib.parse
import urllib.request
import json
from text_analyser import text_analyser
from functions import *
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, WebKit


class HomeWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Home")
        self.set_size_request(950, 600)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.add(scrolled)
        scrolled.add(vbox)
        self.Create_Homepage(vbox)


    def Create_Homepage(self, vbox):
        Entry01 = Gtk.Entry()
        Entry01.set_text("Write something..")
        vbox.pack_start(Entry01, True, True, 0)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        blank_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        blank_box.set_size_request(800, 600)
        vbox.pack_start(blank_box, True, True, 0)

        # button_search_on_web = Gtk.Button.new_with_label("Search on web")
        # button_search_on_web.connect("clicked", self.search, Entry01, hbox)
        # hbox.pack_start(button_search_on_web, True, True, 0)

        button_search = Gtk.Button.new_with_label("Search")
        button_search.connect("clicked", self.Search, Entry01, vbox)
        hbox.pack_start(button_search, True, True, 0)

        # button_search_locally = Gtk.Button.new_with_label("Search locally")
        # #button_search_locally.connect("clicked", self.search_local, LocalSearchScrollView, Entry01)
        # hbox.pack_start(button_search_locally, True, True, 0)

        button_execute = Gtk.Button.new_with_label("Execute")
        button_execute.connect("clicked", self.exec_task, hbox, Entry01)
        hbox.pack_start(button_execute, True, True, 0)


    def Destroy_Homepage(self,vbox):
        for widget in vbox:
            widget.destroy()


    def Create_WebView(self,output_box, text):
        print("Creating webview inside Create_WebView function...")
        url = "https://www.google.co.in/search?q="
        words_to_search = text.split()
        search_keywords = ""
        for word in words_to_search:
            search_keywords += word + '+'
        url = url + search_keywords
        WebViewBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        view = WebKit.WebView()
        view.open(url)
        WebViewBox.pack_start(view, True, True, 0)
        view.show()
        output_box.pack_start(WebViewBox, True, True, 0)
        WebViewBox.show()



    def Create_LocalSearchScrollView(self, output_box, searchkeywords):
        print("Creating Local search view inside function...")
        LocalSearchScrollView = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(LocalSearchScrollView)
        output_box.pack_start(scrolled, True, True, 0)
        scrolled.show()
        LocalSearchScrollView.show()
        # return LocalSearchScrollView
        print("Searching in local files inside function...")
        button = [0] * 10000
        i = 0
        search_result_filepaths, search_result_filenames = localsearch(searchkeywords)
        for res in search_result_filepaths:
            button[i] = Gtk.Button.new_with_label(search_result_filenames[i])
            button[i].connect("clicked", self.open_file_shown_in_search_result, search_result_filepaths[i])
            LocalSearchScrollView.pack_start(button[i], True, True, 0)
            button[i].show()
            i += 1


    def Create_Outputpage(self, vbox, searchkeywords):
        self.Destroy_Homepage(vbox)
        print("Initialised widgets of vbox destroyed...")
        output_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        output_box.set_size_request(800, 600)
        vbox.pack_start(output_box, True, True, 0)
        output_box.show()

        # Create WebView on Outputpage to show google search result of searck keywords
        self.Create_WebView(output_box, searchkeywords)

        # Create view on Outputpage to show local search result
        self.Create_LocalSearchScrollView(output_box, searchkeywords)


    def Search(self, button, Entry01, vbox):
        search_keywords = Entry01.get_text()
        # Goto next page
        self.Create_Outputpage(vbox, search_keywords)



    # def search_local(self, button, scrolled, Entry01):
    #     # Destroy previous search result
    #     for widget in scrolled:
    #         widget.destroy()
    #     # Get text from the entry box
    #     search_keywords = Entry01.get_text()
    #     print("Searching in local files...")
    #     button = [0] * 10000
    #     i = 0
    #     search_result_filepaths, search_result_filenames = localsearch(search_keywords)
    #     for res in search_result_filepaths:
    #         button[i] = Gtk.Button.new_with_label(search_result_filenames[i])
    #         button[i].connect("clicked", self.open_file_shown_in_search_result, search_result_filepaths[i])
    #         scrolled.pack_start(button[i], True, True, 0)
    #         button[i].show()
    #         i += 1
    #

    def open_file_shown_in_search_result(self, button, filepathh):
        # open_file_in_default_application(filepathh)
        subprocess.call(["xdg-open", filepathh])


    def exec_task(self, button, hbox, Entry01):
        command = Entry01.get_text()
        output = text_analyser(command)


    def search(self, button, Entry01, hbox):
        print("\"Search\" button was clicked")
        line_to_search = Entry01.get_text()
        json_data = google_search(line_to_search)


win = HomeWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
