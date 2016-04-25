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

import os
from gi.repository import Gtk

SHELL_PATH = os.path.dirname(os.path.abspath(__file__))
ABOUT_UI_PATH = SHELL_PATH + "/aboutui.glade"


class AboutPage:
    def __init__(self, window):
        self.ui = Gtk.Builder()
        self.ui.add_from_file(ABOUT_UI_PATH)
        self.dialog = self.ui.get_object("about_dialog")
        self.setup_dialog()
        self.dialog.set_transient_for(window)
        self.dialog.show_all()

    def setup_dialog(self):
        self.dialog.connect("response", self.on_about_dialog_close)

    def on_about_dialog_close(self, dialog, response):
        self.dialog.destroy()
