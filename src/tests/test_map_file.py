import os
import unittest
from map_file import MapFile

dirname = os.path.dirname(__file__)

class TestResults(unittest.TestCase):
    def setUp(self):
        self.test_map = MapFile("test_map.map")
        self.test_file = os.path.join(dirname,"test_map.map")

    def test_data_read_from_file(self):
        data = self.test_map.read_map()
        self.assertIsInstance(data, list)

    def test_parameters_are_correct(self):
        data = self.test_map.parameters()
        self.assertEqual(data[1], 183)
        self.assertEqual(data[2], 277)
        self.assertEqual(data[0][0][0], '@')

    def test_no_file(self):
        test_map2 = MapFile("test_file.map")
        with self.assertRaises(SystemExit) as error:
            test_map2.read_map()
        self.assertIsInstance(error.exception, SystemExit)
