import os, sys, subprocess
import gi
import urllib.parse
import urllib.request
import json
from text_analyser import text_analyser
from functions import *

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

        button_search_on_web = Gtk.Button.new_with_label("Search on web")
        button_search_on_web.connect("clicked", self.search, Entry01, vbox)
        vbox.pack_start(button_search_on_web, True, True, 0)

        button_search_locally = Gtk.Button.new_with_label("Search locally")
        button_search_locally.connect("clicked", self.search_local, vbox, Entry01)
        vbox.pack_start(button_search_locally, True, True, 0)

        button_execute = Gtk.Button.new_with_label("Execute")
        button_execute.connect("clicked", self.exec_task, vbox, Entry01)
        vbox.pack_start(button_execute, True, True, 0)


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
        open_file_in_default_application(filepathh)


    def exec_task(self, button, vbox, Entry01):
        command = Entry01.get_text()
        output = text_analyser(command)


    def search(self, button, Entry01, vbox):
        print("\"Search\" button was clicked")
        line_to_search = Entry01.get_text()
        json_data = google_search(line_to_search)


win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
