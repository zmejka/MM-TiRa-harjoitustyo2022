import os
import unittest
from unittest.mock import patch
import pygame
from main import Main
from jps import Jps
from a_star import AStar
from ui.view import View, Button

os.environ["SDL_VIDEODRIVER"] = "dummy"

class TestMain(unittest.TestCase):
    def setUp(self):
        self.main = Main()
        self.width = 120
        self.height = 120
        self.start_point = (10,10)
        self.end_point = (60,60)
        self.algorithm = 1
        self.heuristic = 2

    def test_start_objects(self):
        pygame.init()
        self.assertIsInstance(self.main.start(), tuple)
        self.assertIsInstance(self.main.start()[1], View)
        pygame.quit()

    def test_start_objects_jps(self):
        self.main.algorithm = 2
        self.assertIsInstance(self.main.start()[6], Jps)
    
    def test_start_objects_a_star(self):
        self.assertIsInstance(self.main.start()[6], AStar)

    @patch('main.input', return_value="2")
    def test_get_map(self, return_value):
        self.main.get_map()
        self.assertEqual(self.main.map_data, 2)
    
    @patch('main.input', return_value1="22")
    def test_get_map(self, return_value1):
        self.main.get_map()
        self.assertEqual(self.main.map_data, 1)
    
    @patch('main.input', return_value="f")
    def test_get_map_wrong_value_replaced(self, return_value):
        self.assertEqual(self.main.map_data, 1)
    
    
    @patch('main.input', return_value="g")
    def test_get_parameters_wrong_value(self, return_value):
        self.main.get_parameters()
        self.assertEqual(self.main.algorithm, 1)
        self.assertEqual(self.main.heuristic, 2)