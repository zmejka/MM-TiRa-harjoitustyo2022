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

    def test_find_path_a_star(self):
        start = (1,1)
        end = (3,3)
        self.assertEqual(self.test_a_star.a_star(start,end,2,1)[1], [(1,1),(2,2),(3,3)])
    
    def test_find_path_dijkstra(self):
        start = (1,1)
        end = (3,3)
        self.assertEqual(self.test_a_star.a_star(start,end,2,3)[1], [(1,1),(2,2),(3,3)])

    def test_no_path_available(self):
        test_data = [['@','@','@','@','@'],
                    ['@','.','@','.','@'],
                    ['@','.','@','.','@'],
                    ['@','.','@','.','@'],
                    ['@','@','@','@','@']]
        test_algorithm = AStar(test_data)
        start = (1,1)
        end = (3,3)
        self.assertEqual(test_algorithm.a_star(start,end,2,1), "Polkua ei löytynyt!")
    
    def test_start_same_as_end(self):
        start = (1,1)
        end = (1,1)
        self.assertEqual(self.test_a_star.a_star(start,end,2,1)[1], [(1,1)])
    
    def test_no_path_available_close_list(self):
        test_data = [['@','@','@','@','@'],
                    ['@','.','.','.','@'],
                    ['@','.','@','.','@'],
                    ['@','.','@','.','@'],
                    ['@','.','@','@','@'],
                    ['@','.','.','.','@'],
                    ['@','@','@','@','@']]
        test_algorithm = AStar(test_data)
        start = (1,3)
        end = (5,3)
        self.assertNotEqual(test_algorithm.a_star(start,end,2,1), "Polkua ei löytynyt!")