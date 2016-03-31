from gi.repository import Gtk
import sys
from homepage import HomePage
from settingspage import PluginSettings
from settingspage import ConfigurePage
from setlog import logger

app_path = ''


class TacronHandler:
    def __init__(self):
        self.shell_ui = Gtk.Builder()
        # Gtk.ApplicationWindow.show_all()
        self.shell_ui.add_from_file("shellui.glade")
        logger.debug("Hello")

    def get_window(self):
        return self.shell_ui.get_object("tacron_window")


class Tacron(Gtk.Application):
    # constructor of the Gtk Application

    def __init__(self):
        Gtk.Application.__init__(self)
        PluginSettings()
        self.window_handler = TacronHandler()

    def do_activate(self):
        window = self.window_handler.get_window()
        window.show_all()
        self.add_window(window)

    def do_startup(self):
        Gtk.Application.do_startup(self)


app = Tacron()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
