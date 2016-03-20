import os, sys, subprocess
import gi
import urllib.parse
import urllib.request
import json
import threading
from text_analyser import text_analyser
from srecog import SpeechRecogniser
from functions import *
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, WebKit


class myThread (threading.Thread):
    def __init__(self, threadID, name, Entry, vbox):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.entry = Entry
        self.vbox = vbox
    def run(self):
        print("Starting " + self.name)
        Call_SpeechRecogniser(self.name, self.entry, self.vbox)
        print("Exiting " + self.name)





class HomeWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Home")
        self.set_size_request(950, 600)
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.add(scrolled)
#
#         navigation_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
#         navigation_bar.set_size_request(950, 25)
#         back_button = Gtk.Button.new_with_label("<")
#         back_button.connect("clicked", self.back_button_signal)
#         forward_button = Gtk.Button.new_with_label(">")
# #        forward_button.connect("clicked", self.forward_button_signal)
#         navigation_bar.pack_start(back_button, True, True, 0)
#         navigation_bar.pack_start(forward_button, True, True, 0)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
#        vbox.pack_start(navigation_bar, True, True, 5)
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

        button_search = Gtk.Button.new_with_label("Search")
        button_search.connect("clicked", self.Search, Entry01, vbox)
        hbox.pack_start(button_search, True, True, 0)
	
        button_search = Gtk.Button.new_with_label("sr")
        button_search.connect("clicked", self.Call_Thread_Handler, Entry01, vbox)
        hbox.pack_start(button_search, True, True, 0)

        button_execute = Gtk.Button.new_with_label("Execute")
        button_execute.connect("clicked", self.exec_task, hbox, Entry01)
        hbox.pack_start(button_execute, True, True, 0)


    def Destroy_Homepage(self,vbox):
        for widget in vbox:
            widget.destroy()


    def back_button_signal_of_webview(self, button, webview):
        if webview.can_go_back():
            webview.go_back()

    def forward_button_signal_of_webview(self, button, webview):
        if webview.can_go_forward():
            webview.go_forward()


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

        nv = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        navigation_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        navigation_bar.set_size_request(950, 25)
        back_button = Gtk.Button.new_with_label("<")
        back_button.connect("clicked", self.back_button_signal_of_webview, view)
        forward_button = Gtk.Button.new_with_label(">")
        forward_button.connect("clicked", self.forward_button_signal_of_webview, view)
        navigation_bar.pack_start(back_button, True, True, 0)
        back_button.show()
        navigation_bar.pack_start(forward_button, True, True, 0)
        forward_button.show()
        navigation_bar.show()
        nv.pack_start(navigation_bar, True, True, 0)
        #output_box.pack_start(nv, True, True, 0)
        #nv.show()



    def Create_LocalSearchScrollView(self, output_box, searchkeywords):
        print("Creating Local search view inside function...")
        LocalSearchScrollView = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(LocalSearchScrollView)
        output_box.pack_start(scrolled, True, True, 0)
        scrolled.show()
        LocalSearchScrollView.show()
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


    def Destroy_Outpage(self, vbox):
        for widget in vbox:
            widget.destroy()


    def Search(self, button, Entry01, vbox):
        search_keywords = Entry01.get_text()
        # Goto next page
        self.Create_Outputpage(vbox, search_keywords)


    def open_file_shown_in_search_result(self, button, filepathh):
        # open_file_in_default_application(filepathh)
        print("Path is "+ filepathh)
        subprocess.call(["xdg-open", filepathh])


    def exec_task(self, button, hbox, Entry01):
        command = Entry01.get_text()
        output = text_analyser(command)


    def search(self, button, Entry01, hbox):
        print("\"Search\" button was clicked")
        line_to_search = Entry01.get_text()
        json_data = google_search(line_to_search)

    def Call_Thread_Handler(self, button, Entry, vbox):
        th = myThread(1, "SR_Thread", Entry, vbox)
        th.start()
        th.join()

def Call_SpeechRecogniser(thread_name, Entry, vbox):
    Sr = SpeechRecogniser()
    settings = {'Main'   : {'recogniser':'Sphinx'},
                'Google' : {'api_key':''}}
    text = Sr.recog(settings)


win = HomeWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
