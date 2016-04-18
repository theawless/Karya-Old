import gi
from .functions import localsearch, open_file_shown_in_search_result, google_search
from .search import Search

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, WebKit, Pango


class HomepageHandler:
    def __init__(self):
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
    print("LOL")
    input_text = search_entry.get_text()
    output = Search(input_text)
    output.show(builder)


class HomePage:
    def __init__(self):
        pass

    def get_homepage_box(self):
        builder_homepage = Gtk.Builder()

        builder_homepage.add_from_file("homepage/homepageui.glade")
        builder_homepage.connect_signals(HomepageHandler())

        home_page_full_box = builder_homepage.get_object("home_box")
        search_btn = builder_homepage.get_object("btn_search")
        search_entry = builder_homepage.get_object("search_entry")

        search_btn.connect("clicked", on_search_btn_clicked, builder_homepage, search_entry)

        # view = WebKit.WebView()
        # webview.add(view)
        # view.open("http://www.google.com")
        # webview.add(view)

        return home_page_full_box
