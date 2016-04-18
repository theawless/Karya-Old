import gi

from .functions import localsearch, open_file_shown_in_search_result

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


def on_search_btn_clicked(button, builder):
    print("LOL")
    # google_search()
    # local_search_view_scrolled_window = builder.get_object("local_search_view_scrolled_window")
    # localsearchscrollview = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    # print("Searching in local files inside function...")
    # i = 0
    # searched = ".pdf"
    # # google_search()
    # search_result_filepaths, search_result_filenames = localsearch(searched)
    # for _ in search_result_filepaths:
    #     button = Gtk.Button.new_with_label((search_result_filepaths[i]))
    #     print(search_result_filenames[i])
    #     button.connect("clicked", open_file_shown_in_search_result, search_result_filenames[i])
    #     localsearchscrollview.pack_start(button, True, True, 0)
    #     i += 1
    # local_search_view_scrolled_window.add(localsearchscrollview)


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

        search_btn.connect("clicked", on_search_btn_clicked, builder_homepage)

        view = WebKit.WebView()
        webview.add(view)
        view.open("http://www.google.com")
        webview.add(view)

        return home_page_full_box

        # win = Gtk.Window()
        # win.add(home_page_full_box)
        # win.connect("delete-event", Gtk.main_quit)
        # win.show_all()
        # Gtk.main()


# h = HomePage()
# h.get_homepage()
