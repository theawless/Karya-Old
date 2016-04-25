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

from sarcina.unit_tests.test_google_search import TestGoogleSearch
from sarcina.unit_tests.test_local_search import TestLocalSearch
from sarcina.unit_tests.test_pluginSettings import TestPluginSettings
from sarcina.unit_tests.test_speechRecogniser import TestSpeechRecogniser


class AllTestSuite:
    def __init__(self):
        # self.test_settings = TestPluginSettings()
        # self.test_stt = TestSpeechRecogniser()
        self.test_ls = TestLocalSearch()
        self.test_gs = TestGoogleSearch()

    def run_all_tests(self):
        # self.test_settings.setUp()
        # self.test_settings.run()
        # print("Settings test finished")
        # self.test_stt.setUp()
        # self.test_stt.run()
        self.test_ls.setUp()
        self.test_ls.run()
        print("Local search test finished")
        self.test_gs.setUp()
        self.test_gs.run()
        print("Global search test finished")
        print("All tests finished")


a = AllTestSuite()
a.run_all_tests()
