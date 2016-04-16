import gi
import threading
from homepage.textanalyser import TextAnalyser
from homepage.functions import *
from shell.configure import PluginSettings

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, WebKit


class HomePage:
    def __init__(self):
        pass
