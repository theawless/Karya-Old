from gi.repository import Gtk
import sys
from homepage import HomePage
from settingspage import PluginSettings
from settingspage import ConfigurePage


class MainWindow(Gtk.ApplicationWindow):
    # constructor: the title is "Welcome to GNOME" and the window belongs
    # to the application app

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Tacron", application=app)

        # change windows from here
        self.add(ConfigurePage().get_configure_box())


class Tacron(Gtk.Application):
    # constructor of the Gtk Application

    def __init__(self):
        Gtk.Application.__init__(self)
        PluginSettings()

    def do_activate(self):
        win = MainWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


app = Tacron()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
