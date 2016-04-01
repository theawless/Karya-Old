from gi.repository import Gtk


class AboutPage:
    def __init__(self, window):
        self.ui = Gtk.Builder()
        self.ui.add_from_file("shell/aboutui.glade")
        self.dialog = self.ui.get_object("about_dialog")
        self.setup_dialog()
        self.dialog.set_transient_for(window)
        self.dialog.show_all()

    def setup_dialog(self):
        self.dialog.connect("response", self.on_about_dialog_close)

    def on_about_dialog_close(self, dialog, response):
        self.dialog.destroy()
