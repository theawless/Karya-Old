import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, WebKit

class EntryWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Entry Demo")
        self.set_size_request(200, 100)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        self.entry = Gtk.Entry()
        self.entry.set_text("Hello World")
        vbox.pack_start(self.entry, True, True, 0)
        
        view = WebKit.WebView()
        vbox.pack_start(view, True, True, 0)
        url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyB0lhXv_RqGJRQnlQ5ZrihDLy3TBrEmjIk%20&cx=017576662512468239146:omuauf_lfve&q=lectures"
        view.open(url)

        button01 = Gtk.Button.new_with_label("Search")
        button01.connect("clicked", self.search)
        vbox.pack_start(button01, True, True, 0)

    def search(self, button):
        print("\"Search\" button was clicked")

win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()




