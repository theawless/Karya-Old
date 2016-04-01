import copy

from gi.repository import Gtk
import configparser


class PluginSettings:
    # A static variable in all instances
    settings = dict()

    def __init__(self):
        PluginSettings.settings = self.load_settings()

    @classmethod
    def default_settings(cls):
        # Default settings, to define the format of config file
        config = configparser.ConfigParser()
        config['Main'] = {'recogniser': 'WITAI'}
        config['Sphinx'] = {'version': 'pocketsphinx'}
        config['Google'] = {'api_key': ''}
        config['WITAI'] = {'api_key': 'A3OGNVOCVIMZVWBWLHSV2WLNO5ASS43J'}
        config['IBM'] = {'username': '', 'password': ''}
        config['ATT'] = {'app_key': '', 'app_secret': ''}
        return config

    @classmethod
    def load_settings(cls):
        # Get the configuration from file and return a dictionary
        config = PluginSettings.default_settings()
        config.read('shell/config.ini')
        dictionary = {}
        for section in config.sections():
            dictionary[section] = {}
            for option in config.options(section):
                dictionary[section][option] = config.get(section, option)
        return dictionary

    @classmethod
    def save_settings(cls, settings):
        # Saving settings given from the parameter
        cls.settings = settings
        config = cls.default_settings()
        config['Main'] = {'recogniser': settings['Main']['recogniser']}
        config['Google'] = {'api_key': settings['Google']['api_key']}
        config['WITAI'] = {'api_key': settings['WITAI']['api_key']}
        config['IBM'] = {'username': settings['IBM']['username'], 'password': settings['IBM']['password']}
        config['ATT'] = {'app_key': settings['ATT']['app_key'], 'app_secret': settings['ATT']['app_secret']}
        # Write new values to the configuration file
        with open('shell/config.ini', 'w+') as configfile:
            config.write(configfile)
            # logger.debug("Saved settings")


class ConfigurePage:
    def __init__(self, window):
        self.settings = copy.deepcopy(PluginSettings.settings)
        self.ui = Gtk.Builder()
        self.ui.add_from_file("shell/configureui.glade")
        self.setup_dialog()

        self.dialog = self.ui.get_object("configure_dialog")
        self.dialog.set_transient_for(window)
        self.dialog.show_all()

    def setup_dialog(self):
        # Setup everything
        self._get_saved_into_text_boxes()
        self._choose_labelled_input_boxes()
        self._connect_everything()
        self._configure_radios()

    def on_close_dialog(self, button):
        self.dialog.destroy()

    def _get_saved_into_text_boxes(self):
        _settings = self.settings
        self.ui.get_object("google_key_entry").set_text(_settings['Google']['api_key'])
        self.ui.get_object("witai_key_entry").set_text(_settings['WITAI']['api_key'])
        self.ui.get_object("ibm_username_entry").set_text(_settings['IBM']['username'])
        self.ui.get_object("ibm_password_entry").set_text(_settings['IBM']['password'])
        self.ui.get_object("att_api_entry").set_text(_settings['ATT']['app_key'])
        self.ui.get_object("att_secret_entry").set_text(_settings['ATT']['app_secret'])

    def _connect_everything(self):
        # Connecting all radios,buttons to the callback function
        self.ui.get_object("sphinx_radio").connect("toggled", self._radio_callback, "Sphinx")
        self.ui.get_object("google_radio").connect("toggled", self._radio_callback, "Google")
        self.ui.get_object("witai_radio").connect("toggled", self._radio_callback, "WITAI")
        self.ui.get_object("att_radio").connect("toggled", self._radio_callback, "ATT")
        self.ui.get_object("ibm_radio").connect("toggled", self._radio_callback, "IBM")
        self.ui.get_object("save_button").connect("clicked", self._confirm_config)
        self.ui.get_object("default_button").connect("clicked", self._set_default_config)
        self.ui.get_object("close_button").connect("clicked", self.on_close_dialog)

    def _configure_radios(self):
        # Load the radio buttons with settings
        _settings = self.settings

        if _settings['Main']['recogniser'] == "Sphinx":
            self.ui.get_object("sphinx_radio").set_active(True)
        elif _settings['Main']['recogniser'] == "Google":
            self.ui.get_object("google_radio").set_active(True)
        elif _settings['Main']['recogniser'] == "WITAI":
            self.ui.get_object("witai_radio").set_active(True)
        elif _settings['Main']['recogniser'] == "IBM":
            self.ui.get_object("ibm_radio").set_active(True)
        elif _settings['Main']['recogniser'] == "ATT":
            self.ui.get_object("att_radio").set_active(True)

    def _choose_labelled_input_boxes(self):
        # choosing input box
        self.ui.get_object("google_box").set_sensitive(False)
        self.ui.get_object("ibm_box").set_sensitive(False)
        self.ui.get_object("att_box").set_sensitive(False)
        self.ui.get_object("witai_box").set_sensitive(False)
        # Disabled everything"

        data = self.settings['Main']['recogniser']
        if data == 'Google':
            self.ui.get_object("google_box").set_sensitive(True)
        elif data == 'WITAI':
            self.ui.get_object("witai_box").set_sensitive(True)
        elif data == 'ATT':
            self.ui.get_object("att_box").set_sensitive(True)
        elif data == 'IBM':
            self.ui.get_object("ibm_box").set_sensitive(True)

    def _radio_callback(self, radio, data):
        # Define what happens when Radio options are selected
        # logger.debug("%s was toggled %s" % (data, ("OFF", "ON")[widget.get_active()]))
        if radio.get_active():
            # All radio_callback are called simultaneously, checking which one went active
            self.settings['Main']['recogniser'] = data
            self._choose_labelled_input_boxes()

    def _set_default_config(self, button):
        # load default settigns and save them by calling PluginSetting
        self.settings = PluginSettings.default_settings()
        PluginSettings.save_settings(self.settings)
        self._get_saved_into_text_boxes()
        self._configure_radios()

    def _confirm_config(self, button):
        # save input values to temporary settings
        self.settings['Google']['api_key'] = self.ui.get_object("google_key_entry").get_text()
        self.settings['WITAI']['api_key'] = self.ui.get_object("witai_key_entry").get_text()
        self.settings['IBM']['username'] = self.ui.get_object("ibm_username_entry").get_text()
        self.settings['IBM']['password'] = self.ui.get_object("ibm_password_entry").get_text()
        self.settings['ATT']['app_key'] = self.ui.get_object("att_api_entry").get_text()
        self.settings['ATT']['app_secret'] = self.ui.get_object("att_secret_entry").get_text()
        # save to PluginClass
        PluginSettings.save_settings(self.settings)
