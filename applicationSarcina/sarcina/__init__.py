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

import sys

from gi.repository import Gtk

from sarcina.setlog import logger
from sarcina.shell.aboutpage import AboutPage
from sarcina.shell.configure import ConfigurableDialog
from sarcina.shell.configure import PluginSettings
from sarcina.homepage.homepage import HomePage
from sarcina.taskerpage.taskerpage import TaskerPage


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
        taskerpage_box = self.shell_ui.get_object("tasker_notebook_box")
        home = HomePage()
        tasker = TaskerPage()
        homepage_box.add(home.get_homepage_box())
        taskerpage_box.add(tasker.get_taskerpage_box())
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
