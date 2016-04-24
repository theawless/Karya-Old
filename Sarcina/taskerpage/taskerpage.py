import gi
import sys

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from taskerpage.mysql_scripts import delete, fetchData
from taskerpage.mysql_scripts.insert import insert

sys.path.insert(0, '/home/abhinavp/Desktop/working_dir/Sarcina/lexical_analyser/')
import textanalyser


class TaskerHandler:
    def __init__(self):
        pass


x = "test_script.py"


class TaskerPage:
    """
    Class to preview and set tasks
    """
    def __init__(self):
        """
        Initialize variables
        :return: null
        """
        self.name_of_curr_script = ""
        self.script_inst = None

    def on_set_btn_clicked(self, button, entry, entry_name):
        """
        Sets script for execution
        :param button:
        :param entry:
        :param entry_name:
        :return: null
        """
        input_name = entry_name.get_text()
        self.script_inst.set_written_script()
        insert(input_name, self.name_of_curr_script)

    def on_preview_btn_clicked(self, button, entry, label_preview):
        """
        Shows preview of generated script by script writer
        :param button:
        :param entry:
        :param label_preview:
        :return: null
        """
        input_text = entry.get_text()
        print("hello" + input_text)
        self.name_of_curr_script, script_inst = textanalyser.textanalyser(input_text)
        fp = open(self.name_of_curr_script).read()
        self.script_inst = script_inst
        label_preview.set_text(fp)

    def on_set_task_clicked(self, param1, param2):
        """
        Handler when existing task is clicked
        :param param1:
        :param param2:
        :return:
        """
        print("On set task clicked")

    def get_taskerpage_box(self):
        """
        Shows scripts to the page loaded from database
        :return: null
        """
        builder_homepage = Gtk.Builder()

        builder_homepage.add_from_file("taskerpage/taskerpageui.glade")
        builder_homepage.connect_signals(TaskerHandler())

        home_page_full_box = builder_homepage.get_object("tasker_box")
        set_btn = builder_homepage.get_object("set_btn")
        preview_btn = builder_homepage.get_object("preview_btn")
        input = builder_homepage.get_object("input_entry")
        preview_of_task = builder_homepage.get_object("preview_label")
        entry_name = builder_homepage.get_object("entry_name")
        tasks_view = builder_homepage.get_object("tasks")

        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        hbox.set_homogeneous(False)
        tasks = fetchData.fetchData()
        for task in tasks:
            tempBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
            tempLabel = Gtk.Label(task["name"])
            tempButton = Gtk.Button.new_with_label("Set Task")
            tempButton.connect("clicked", self.on_set_task_clicked, task["file_location"])
            tempBox.pack_start(tempLabel, True, True, 0)
            tempBox.pack_start(tempButton, True, True, 0)
            hbox.pack_start(tempBox, True, True, 0)
        tasks_view.add(hbox)

        set_btn.connect("clicked", self.on_set_btn_clicked, input, entry_name)
        preview_btn.connect("clicked", self.on_preview_btn_clicked, input, preview_of_task)

        return home_page_full_box
