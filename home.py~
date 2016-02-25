import gi
import urllib.parse
import urllib.request
import json

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, WebKit


class EntryWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Entry Demo")
        self.set_size_request(200, 100)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        Entry01 = Gtk.Entry()
        Entry01.set_text("Write something..")
        vbox.pack_start(Entry01, True, True, 0)
#        url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyB0lhXv_RqGJRQnlQ5ZrihDLy3TBrEmjIk%20&cx=017576662512468239146:omuauf_lfve&q="
        url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyDKXPuaXh84T_tVVQcxQdbQS8TzNk2uuuU%20&cx=017576662512468239146:omuauf_lfve&q="
#        view = WebKit.WebView()

#        view.open(url)
#        vbox.pack_start(view, True, True, 0)

        button01 = Gtk.Button.new_with_label("Search")
        button01.connect("clicked", self.search, url, Entry01, vbox)
        vbox.pack_start(button01, True, True, 0)

        button02 = Gtk.Button.new_with_label("Show links from search result")
        button02.connect("clicked", self.showlinks, vbox)
        vbox.pack_start(button02, True, True, 0)

    def search(self, button, url, Entry01, vbox):
        print("\"Search\" button was clicked")
        search_keywords = Entry01.get_text()
        url = url + search_keywords
        print("URL is : "+url)
        response = urllib.request.urlopen(url)
        content = response.read()
        data = json.loads(content.decode("utf8"))
        for i in data['items']:
            print(i['title'])
            print(i['link'])
            print(i['snippet'])

    def showlinks(self, button, vbox):
        print("none")
#        button03 = Gtk.Button.new_with_label("test successfull")
#        vbox.pack_start(button03, True, True, 0)

win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()




