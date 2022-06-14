import os
import unittest
import pygame
from main import Main
from jps import Jps
from a_star import AStar
from ui.view import View

os.environ["SDL_VIDEODRIVER"] = "dummy"

class TestMain(unittest.TestCase):
    def setUp(self):
        self.main = Main(1,1,2)
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

