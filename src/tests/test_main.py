import os
import unittest
import pygame
from main import Main
from ui.view import View

os.environ["SDL_VIDEODRIVER"] = "dummy"

class TestMain(unittest.TestCase):
    def setUp(self):
        self.main = Main()
        self.width = 120
        self.height = 120
        self.start_point = (10,10)
        self.end_point = (60,60)

    def test_start_objects(self):
        pygame.init()
        self.assertIsInstance(self.main.start(), tuple)
        self.assertIsInstance(self.main.start()[1], View)
        pygame.quit()

