import gi
from .functions import localsearch, open_file_shown_in_search_result, google_search

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
    # google_search(input_text)

    list_box = builder.get_object("list_box")

    print("Searching in local files inside function...")
    searched = input_text
    #google_search()
    tup_list = localsearch(searched)
    for (filepath, filename) in tup_list:
        label = Gtk.Label(filename)
        label.set_single_line_mode(True)
        label.set_line_wrap_mode(Pango.WrapMode.CHAR)
        button = Gtk.Button.new_with_label("Open")
        button.connect("clicked", open_file_shown_in_search_result, filename)
        row = Gtk.ListBoxRow()
        hbox = Gtk.HBox()
        hbox.set_homogeneous(True)
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(button, True, False, 0)
        row.add(hbox)
        list_box.prepend(row)

    list_box.show_all()


class HomePage:
    def __init__(self):
        pass

    def get_homepage_box(self):
        builder_homepage = Gtk.Builder()

        builder_homepage.add_from_file("homepage/homepageui.glade")
        builder_homepage.connect_signals(HomepageHandler())

        home_page_full_box = builder_homepage.get_object("home_box")
        webview = builder_homepage.get_object("webview_scrolled_window")
        search_btn = builder_homepage.get_object("btn_search")
        search_entry = builder_homepage.get_object("search_entry")

        search_btn.connect("clicked", on_search_btn_clicked, builder_homepage, search_entry)

        view = WebKit.WebView()
        webview.add(view)
        view.open("http://www.google.com")
        webview.add(view)

        return home_page_full_box