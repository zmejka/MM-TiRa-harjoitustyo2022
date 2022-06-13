import unittest
from algorithm_core import AlgorithmCore
from jps import Jps

class TestAStar(unittest.TestCase):
    def setUp(self):
        self.data = [['@','@','@','@','@'],
                    ['@','.','.','.','@'],
                    ['@','.','.','.','@'],
                    ['@','.','.','.','@'],
                    ['@','@','@','@','@']]
        self.test_jps = Jps(self.data)

    def test_find_path_available(self):
        start = (1,1)
        end = (3,3)
        self.assertEqual(self.test_jps.jps(start,end)[1], [(1,1),(3,3)])

    def test_no_path_available(self):
        test_data = [['@','@','@','@','@'],
                    ['@','.','@','.','@'],
                    ['@','.','@','.','@'],
                    ['@','.','@','.','@'],
                    ['@','@','@','@','@']]
        test_algorithm = Jps(test_data)
        start = (1,1)
        end = (3,3)
        self.assertEqual(test_algorithm.jps(start,end), "Polkua ei löytynyt!")
    
    def test_diagonal_jumps_hor(self):
        test_data = [['@','@','@','@','@'],
                    ['@','.','.','.','@'],
                    ['@','@','@','.','@'],
                    ['@','.','.','.','@'],
                    ['@','@','@','@','@']]
        test_algorithm = Jps(test_data)
        start = (1,1)
        end = (3,3)
        self.assertEqual(test_algorithm.jps(start,end)[1], [(1,1),(1,2),(2,3),(3,3)])
    
    def test_diagonal_jumps_ver(self):
        test_data = [['@','@','@','@','@'],
                    ['@','.','@','.','@'],
                    ['@','.','@','.','@'],
                    ['@','.','.','.','@'],
                    ['@','@','@','@','@']]
        test_algorithm = Jps(test_data)
        start = (1,1)
        end = (3,3)
        self.assertEqual(test_algorithm.jps(start,end)[1], [(1,1),(2,1),(3,2),(3,3)])
    
    def test_start_same_as_end(self):
        start = (1,1)
        end = (1,1)
        self.assertEqual(self.test_jps.jps(start,end)[1], [(1,1)])