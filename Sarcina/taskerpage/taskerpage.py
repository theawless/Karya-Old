import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class TaskerHandler:
    def __init__(self):
        pass


def on_set_btn_clicked(button, entry):
    input_text = entry.get_text()
    print(input_text)


def on_preview_btn_clicked(button, entry):
    input_text = entry.get_text()
    print("hello" + input_text)


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

        set_btn.connect("clicked", on_set_btn_clicked, input)
        preview_btn.connect("clicked", on_preview_btn_clicked, input)

        return home_page_full_box
