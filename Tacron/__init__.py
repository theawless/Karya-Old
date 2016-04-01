from gi.repository import Gtk
import sys
from homepage.homepage import HomePage
from shell.configure import PluginSettings
from shell.configure import ConfigurePage
from setlog import logger
from shell.aboutpage import AboutPage

app_path = ''


class TacronHandler:
    def __init__(self, shell_ui):
        self.shell_ui = shell_ui


class Tacron(Gtk.Application):
    # constructor of the Gtk Application

    def __init__(self):
        Gtk.Application.__init__(self)
        PluginSettings()
        self.shell_ui = Gtk.Builder()
        self.shell_ui.add_from_file("shell/shellui.glade")
        self.window_handler = TacronHandler(self.shell_ui)
        self.handler_dict = {
            "on_about_image_menu_item_activate": self.on_about_activate,
            "on_pref_image_menu_item_activate": self.on_pref_activate,
            "on_quit_image_menu_item_activate": self.on_quit_activate
        }
        self.shell_ui.connect_signals(self.handler_dict)

    def do_activate(self):
        window = self.shell_ui.get_object("tacron_window")
        self.add_window(window)
        window.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def on_about_activate(self, menu_item):
        logger.debug(self.shell_ui.get_object("tacron_window").get_default_size())

        AboutPage(self.shell_ui.get_object("tacron_window"))

    def on_pref_activate(self, menu_item):
        ConfigurePage(self.shell_ui.get_object("tacron_window"))

    def on_quit_activate(self, menu_item):
        sys.exit()


app = Tacron()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
