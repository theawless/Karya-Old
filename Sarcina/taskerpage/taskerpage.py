import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from taskerpage.mysql_scripts import delete, fetchData
from taskerpage.mysql_scripts.insert import insert


class TaskerHandler:
    def __init__(self):
        pass


x = "test_script.py"


def on_set_btn_clicked(button, entry, entry_name):
    input_text = entry.get_text()
    input_name = entry_name.get_text()
    insert(input_name, x)
    print(input_text)


def on_preview_btn_clicked(button, entry):
    input_text = entry.get_text()
    print("hello" + input_text)


def on_click_me_clicked(button, index):
    delete.delete(index)


class TaskerPage:
    def __init__(self):
        pass

    def get_taskerpage_box(self):
        builder_homepage = Gtk.Builder()

        builder_homepage.add_from_file("taskerpage/taskerpageui.glade")
        builder_homepage.connect_signals(TaskerHandler())

        home_page_full_box = builder_homepage.get_object("tasker_box")
        set_btn = builder_homepage.get_object("set_btn")
        preview_btn = builder_homepage.get_object("preview_btn")
        input = builder_homepage.get_object("input_entry")
        preview_of_task = builder_homepage.get_object("preview_of_task")
        entry_name = builder_homepage.get_object("entry_name")
        tasks_view = builder_homepage.get_object("tasks")

        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        hbox.set_homogeneous(False)
        tasks = fetchData.fetchData()
        for task in tasks:
            tempBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
            tempLabel = Gtk.Label(task["name"])
            # tempButton = Gtk.Button.new_with_label("Delete Task")
            # tempButton.connect("clicked", on_click_me_clicked, int(task["index"]))
            tempBox.pack_start(tempLabel, True, True, 0)
            # tempBox.pack_start(tempButton, True, True, 0)
            hbox.pack_start(tempBox, True, True, 0)
        tasks_view.add(hbox)

        set_btn.connect("clicked", on_set_btn_clicked, input)
        preview_btn.connect("clicked", on_preview_btn_clicked, input)

        return home_page_full_box
