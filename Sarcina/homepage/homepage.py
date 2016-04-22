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
        print("Search button :D :D")
        # def on_entrybuffer1_deleted_text(self, entrybuffer):
        #     pass
        #
        # def on_entrybuffer1_inserted_text(self, entrybuffer):
        #     pass
        #
        # def on_entrycompletion1_action_activated(self, entrycompletion):
        #     pass
        #
        # def on_entrycompletion1_cursor_on_match(self, entrycompletion):
        #     pass
        #
        # def on_entrycompletion1_insert_prefix(self, entrycompletion):
        #     pass
        #
        # def on_entrycompletion1_match_selected(self, entrycompletion):
        #     pass
        #
        # def on_SearchEntry_insert_text(self, SearchEntry):
        #    pass


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
        time.sleep(1)
        self.recogniser = SpeechRecogniser(self.search_entry_bar_text_changer)
        logger.debug("Constructed recogniser, Inside __init__ of homepage")
        self.threader = threading.Thread(target=self.recogniser.start_recognising)
        self.threader.daemon = True
        self.threader.start()
        pass

    def search_entry_bar_text_changer(self, text: str):
        """
        displays the recognized text in search entry
        :type text: basestring
        :param text: recognized text
        :return: Null
        """
        search_entry = self.builder.get_object("search_entry")
        search_entry.set_text(text)

    def get_homepage_box(self):
        """
        creates view of homepage tab of notebook and connects its signals to implemented functions.
        :return: Gtk box widget
        """
        self.builder.add_from_file("homepage/homepageui.glade")
        self.builder.connect_signals(HomepageHandler())

        home_page_full_box = self.builder.get_object("home_box")
        search_btn = self.builder.get_object("btn_search")
        search_entry = self.builder.get_object("search_entry")

        search_btn.connect("clicked", on_search_btn_clicked, self.builder, search_entry)

        # view = WebKit.WebView()
        # webview.add(view)
        # view.open("http://www.google.com")
        # webview.add(view)

        return home_page_full_box
