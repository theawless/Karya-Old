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

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from sarcina.taskerpage.mysql_scripts import fetchData

from sarcina.taskerpage.mysql_scripts import delete


class LabelWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Label Example")

        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        hbox.set_homogeneous(False)
        tasks = fetchData.fetchData()
        for task in tasks:
            tempBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
            tempLabel = Gtk.Label(task["name"])

            tempButton = Gtk.Button.new_with_label("Delete Task")
            tempButton.connect("clicked", self.on_click_me_clicked, int(task["index"]))

            tempBox.pack_start(tempLabel, True, True, 0)
            tempBox.pack_start(tempButton, True, True, 0)

            hbox.pack_start(tempBox, True, True, 0)

        self.add(hbox)

    def on_click_me_clicked(self, button, index):
        delete.delete(index)


window = LabelWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
