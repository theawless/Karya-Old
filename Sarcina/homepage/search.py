import gi
from gi.repository import Gtk, Pango

from homepage.functions import open_file_shown_in_search_result, local_search, google_search
import urllib

gi.require_version('Gtk', '3.0')


def clean(widget_view):
    for widget in widget_view:
        widget.destroy()


def show_local_search_result(builder, input_text):
    """
    shows search result in GUI after searching in local directories
    :param builder: auxiliary object to access the widgets in the interface by the names assigned to them
    :type input_text: basestring
    :param input_text: text to search
    :return: NULL
    """
    search_res_listbox = builder.get_object("list_box")
    clean(search_res_listbox)
    tup_list = local_search(input_text)
    for (path, name) in tup_list:
        label = Gtk.Label(name)
        label.set_single_line_mode(True)
        label.set_line_wrap_mode(Pango.WrapMode.CHAR)
        button = Gtk.Button.new_with_label("Open")
        button.connect("clicked", open_file_shown_in_search_result, path)
        row = Gtk.ListBoxRow()
        hbox = Gtk.HBox()
        hbox.set_homogeneous(True)
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(button, True, False, 0)
        row.add(hbox)
        search_res_listbox.prepend(row)
    search_res_listbox.show_all()


def show_google_results(builder, text):
    """
    takes google search result in JSON and displays in GUI
    :param builder: auxiliary object to access the widgets in the interface by the names assigned to them
    :type text: basestring
    :param text: text to search
    :return: NULL
    """
    web_res = builder.get_object("web_res_listbox")
    clean(web_res)
    try:
        data = google_search(text)
        for i in data['items']:
            label_title = Gtk.Label()
            label_snippet = Gtk.Label(i['snippet'])
            markup = "<a href=\"" + str(i['link']) + "\"" + ">" + str(i['title']) + "</a>."
            label_title.set_markup(markup)
            row = Gtk.ListBoxRow()
            vbox = Gtk.VBox()
            vbox.pack_start(label_title, True, True, 0)
            vbox.pack_start(label_snippet, True, True, 0)
            row.add(vbox)
            web_res.prepend(row)
            print(i['title'])
            print(i['link'])
            print(i['snippet'])
    except urllib.error.URLError:
        print("Check proxy!! urllib.error.URLError in google search :(  :( ")
    web_res.show_all()


class Search:
    """
    This class represent a class for search query
    """

    def __init__(self, text):
        """
        creates the variable associated with the class
        :type text: basestring
        :param text:  text to search
        """
        self.text = text

    def show(self, builder):
        """

        :param builder:  auxiliary object to access the widgets in the interface by the names assigned to them
        :return: NULL
        """
        show_google_results(builder, self.text)
        show_local_search_result(builder, self.text)
