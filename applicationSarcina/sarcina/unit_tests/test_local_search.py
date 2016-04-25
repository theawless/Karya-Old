from unittest import TestCase
from sarcina.homepage.functions import local_search


class TestLocalSearch(TestCase):
    def setUp(self):
        self.input_keyword1 = "hello.txt"
        self.input_keyword2 = "file23"
        self.input_keyword3 = "file54"

    def run(self, result=None):
        self.assertEqual(local_search(self.input_keyword1), [('../../../../Desktop/Search_res/hello.txt', 'hello.txt'),
                                                             (
                                                                 '../../../../Desktop/Search_res/hello.txt~',
                                                                 'hello.txt~')]
                         )
        self.assertEqual(local_search(self.input_keyword2), [('../../../../Desktop/Search_res/file23', 'file23'),
                                                             ('../../../../Desktop/Search_res/file23~', 'file23~')]
                         )
        self.assertEqual(local_search(self.input_keyword3), [('../../../../Desktop/Search_res/file54', 'file54')])
