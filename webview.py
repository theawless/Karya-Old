import os, sys, subprocess
import gi
from urlparse import urlparse
import urllib2
from urllib2 import Request
import json

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, WebKit


class EntryWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Tasker")
        self.set_size_request(200, 100)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        Entry01 = Gtk.Entry()
        vbox.pack_start(Entry01, True, True, 0)
        view = WebKit.WebView()
        view.open("https://www.google.com")
        vbox.pack_start(view, True, True, 0)

win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

