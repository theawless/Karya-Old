import gi
from gi.repository import Gtk, Pango

from homepage.functions import open_file_shown_in_search_result, localsearch, google_search

gi.require_version('Gtk', '3.0')


def show_local_search_result(builder, input_text):
    search_res_listbox = builder.get_object("list_box")
    tup_list = localsearch(input_text)
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
        search_res_listbox.prepend(row)
    search_res_listbox.show_all()


def show_google_results(builder, text):
    web_res = builder.get_object("web_res_listbox")
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
    web_res.show_all()


class Search:
    def __init__(self, text):
        self.text = text

    def show(self, builder):
        show_google_results(builder, self.text)
        show_local_search_result(builder, self.text)
