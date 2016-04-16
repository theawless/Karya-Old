# Dict'O'nator - A dictation plugin for gedit.
# Copyright (C) <2016>  <Abhinav Singh>
#
# This file is part of Dict'O'nator.
#
# Dict'O'nator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Dict'O'nator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Dict'O'nator.  If not, see <http://www.gnu.org/licenses/>.

from .test_pluginSettings import TestPluginSettings
from .test_speechRecogniser import TestSpeechRecogniser


class AllTestSuite:
    def __init__(self):
        self.test_settings = TestPluginSettings()
        self.test_stt = TestSpeechRecogniser()

    def run_all_tests(self):
        self.test_settings.setUp()
        self.test_settings.run()
        print("Settings test finished")
        self.test_stt.setUp()
        self.test_stt.run()
        print("All tests finished")


a = AllTestSuite()
a.run_all_tests()
