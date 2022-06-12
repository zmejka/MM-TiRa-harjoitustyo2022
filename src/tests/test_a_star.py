import unittest
from algorithm_core import AlgorithmCore
from a_star import AStar

class TestAStar(unittest.TestCase):
    def setUp(self):
        self.data = [['@','@','@','@','@'],
                    ['@','.','.','.','@'],
                    ['@','.','.','.','@'],
                    ['@','.','.','.','@'],
                    ['@','@','@','@','@']]
        self.test_a_star = AStar(self.data)
        self.test_core = AlgorithmCore(self.data)

    def test_start(self):
        pass
