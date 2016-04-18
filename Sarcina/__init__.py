import sys

from gi.repository import Gtk

from setlog import logger
from shell.aboutpage import AboutPage
from shell.configure import ConfigurableDialog
from shell.configure import PluginSettings
from homepage.homepage import HomePage

class SarcinaHandler:
    def __init__(self, shell_ui):
        self.shell_ui = shell_ui


class Sarcina(Gtk.Application):
    # constructor of the Gtk Application

    def __init__(self):
        Gtk.Application.__init__(self)
        PluginSettings()
        self.shell_ui = Gtk.Builder()
        self.shell_ui.add_from_file("shell/shellui.glade")
        self.window_handler = SarcinaHandler(self.shell_ui)
        self.handler_dict = {
            "on_about_image_menu_item_activate": self.on_about_activate,
            "on_pref_image_menu_item_activate": self.on_pref_activate,
            "on_quit_image_menu_item_activate": self.on_quit_activate
        }
        self.shell_ui.connect_signals(self.handler_dict)

    def do_activate(self):
        window = self.shell_ui.get_object("sarcina_window")
        homepage_box = self.shell_ui.get_object("home_notebook_box")
        home = HomePage()
        homepage_box.add(home.get_homepage_box())
        self.add_window(window)
        window.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def on_about_activate(self, menu_item):
        logger.debug(self.shell_ui.get_object("sarcina_window").get_default_size())
        AboutPage(self.shell_ui.get_object("sarcina_window"))

    def on_pref_activate(self, menu_item):
        ConfigurableDialog(self.shell_ui.get_object("sarcina_window"))

    def on_quit_activate(self, menu_item):
        sys.exit()


app = Sarcina()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
