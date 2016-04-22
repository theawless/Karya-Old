import threading

import gi
import time

from homepage.recogspeechbg import SpeechRecogniser
from homepage.setlog import logger
from .search import Search

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class HomepageHandler:
    """
    This is a signal handler class for homepage
    """

    def __init__(self):
        """
        constructor of HomepageHandler
        :return: NULL
        """
        pass

    def on_btn_search_clicked(self, button):
        pass


def on_search_btn_clicked(button, builder, search_entry):
    """
    creates an object of class type Search and calls its member function to show output on homepage
    :param button:
    :param builder:  auxiliary object to access the widgets in the interface by the names assigned to them
    :type search_entry: basestring
    :param search_entry: input text
    :return: NULL
    """
    input_text = search_entry.get_text()
    output = Search(input_text)
    output.show(builder)


class HomePage:
    """
    This class represent a class for Homepage of Sarcina
    """

    def __init__(self):
        """
        Constructor of HomePage
        :return: NULL
        """
        self.builder = Gtk.Builder()
        self.builder.add_from_file("homepage/homepageui.glade")
        self.builder.connect_signals(HomepageHandler())
        self.search_entry = self.builder.get_object("search_entry")
        self.search_btn = self.builder.get_object("btn_search")
        self.home_page_full_box = self.builder.get_object("home_box")
        self.status_label = self.builder.get_object("status_label")
        self.recognised_text = ""
        self.start_recog()

    def start_recog(self):
        time.sleep(1)
        recogniser = SpeechRecogniser(self.do_after_recog, self.status_text_set)
        logger.debug("Constructed recogniser, Inside __init__ of homepage")
        threader = threading.Thread(target=recogniser.start_recognising)
        threader.daemon = True
        threader.start()

    def do_after_recog(self, text: str):
        self.recognised_text = text
        self.analyse_text()
        self.search_entry_bar_text_changer(self.recognised_text)

    def analyse_text(self):
        self.status_text_set("Recognised text" + self.recognised_text)
        output = Search(self.recognised_text)
        output.show(self.builder)

    def search_entry_bar_text_changer(self, text: str):
        """
        displays the recognized text in search entry
        :type text: basestring
        :param text: recognized text
        :return: Null
        """
        search_entry = self.builder.get_object("search_entry")
        search_entry.set_text(text)

    def status_text_set(self, text: str):
        """
        displays the recognized text in search entry
        :type text: basestring
        :param text: recognized text
        :return: Null
        """
        self.status_label.set_text(text)

    def get_homepage_box(self):
        """
        creates view of homepage tab of notebook and connects its signals to implemented functions.
        :return: Gtk box widget
        """
        self.search_btn.connect("clicked", on_search_btn_clicked, self.builder, self.search_entry)
        return self.home_page_full_box
