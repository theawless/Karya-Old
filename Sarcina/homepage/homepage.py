import gi
from _cffi_backend import string

import subprocess
from functions import localsearch

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, WebKit


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


class HomePage:
    def __init__(self):
        pass

    def open_file_shown_in_search_result(self, button, filepathh):
        # open_file_in_default_application(filepathh)
        print("Path is " + filepathh)
        subprocess.call(["xdg-open", filepathh])

    def get_homepage(self):
        builder = Gtk.Builder()

        builder.add_from_file("homepageui.glade")
        builder.connect_signals(HomepageHandler())

        home_page_full_box = builder.get_object("home_box")
        webview = builder.get_object("webview_scrolled_window")
        local_search_view_scrolled_window = builder.get_object("local_search_view_scrolled_window")

        # local_search_view.add(button_search)
        view = WebKit.WebView()
        webview.add(view)
        view.open("http://www.google.com")
        webview.add(view)

        # scrolled_parent = Gtk.ScrolledWindow()
        # scrolled_parent.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        # scrolled_parent.add(localsearchscrollview)
        localsearchscrollview = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        # scrolled = Gtk.ScrolledWindow()
        # scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        print("Searching in local files inside function...")
        i = 0
        searched = ".pdf"
        # google_search()
        search_result_filepaths, search_result_filenames = localsearch(searched)
        assert isinstance(search_result_filepaths, object)

        for s in search_result_filepaths:
            button = Gtk.Button.new_with_label((search_result_filepaths[i]))
            print(search_result_filenames[i])
            button.connect("clicked", self.open_file_shown_in_search_result, search_result_filenames[i])
            localsearchscrollview.pack_start(button, True, True, 0)
            i += 1
        local_search_view_scrolled_window.add(localsearchscrollview)

        win = Gtk.Window()
        win.add(home_page_full_box)
        win.connect("delete-event", Gtk.main_quit)
        win.show_all()
        Gtk.main()


        # x = builder.get_object("home_pane")
        # return x


h = HomePage()
h.get_homepage()
