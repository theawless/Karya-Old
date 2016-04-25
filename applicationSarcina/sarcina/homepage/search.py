# Sarcina - A voice based tasker/assistant for Ubuntu.
# Copyright (C) <2016>  <Abhinav Singh>
# Copyright (C) <2016>  <Abhinav Prince>
# Copyright (C) <2016>  <Harshit Rai>
# Copyright (C) <2016>  <Suraj Jha>
#
# This file is part of Sarcina.
#
# Sarcina is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Sarcina is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Sarcina.  If not, see <http://www.gnu.org/licenses/>.

import gi
from gi.repository import Gtk, Pango

from sarcina.homepage.functions import open_file_shown_in_search_result, local_search, google_search
import urllib
import urllib.error
gi.require_version('Gtk', '3.0')


def clean(widget_view):
    """
    destroy all widgets inside the view
    :param widget_view: box containing widgets of gui
    :return: None
    """
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
        asks google and locaL search engine to display results
        :param builder:  auxiliary object to access the widgets in the interface by the names assigned to them
        :return: NULL
        """
        show_google_results(builder, self.text)
        show_local_search_result(builder, self.text)
