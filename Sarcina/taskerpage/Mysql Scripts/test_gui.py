import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import fetchData
import delete

class LabelWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Label Example")
        
        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        hbox.set_homogeneous(False)
        tasks = fetchData.fetchData()
        for task in tasks:
            tempBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=10)
            tempLabel = Gtk.Label(task["name"])

            tempButton = Gtk.Button.new_with_label("Delete Task")
            tempButton.connect("clicked", self.on_click_me_clicked,int(task["index"]))

            tempBox.pack_start(tempLabel, True, True, 0)
            tempBox.pack_start(tempButton, True, True, 0)

            hbox.pack_start(tempBox,True,True,0)

        self.add(hbox)

    def on_click_me_clicked(self,button,index):
        delete.delete(index)

window = LabelWindow()        
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()