import unittest
from algorithm_core import AlgorithmCore

class TestAlgorithmCore(unittest.TestCase):
    def setUp(self):
        self.data = [['@','@','@','@','@'],
                    ['@','.','.','.','@'],
                    ['@','.','.','.','@'],
                    ['@','.','.','.','@'],
                    ['@','@','@','@','@']]
        self.test_core = AlgorithmCore(self.data)

    def test_set_map(self):
        test_map = [['@','.','@'],['@','.','.'],['.','.','@']]
        self.test_core.set_map(test_map)
        self.assertEqual(self.test_core.map_data, [['@','.','@'],['@','.','.'],['.','.','@']])
    
    def test_get_map(self):
        self.assertEqual(self.test_core.get_map(), [['@','@','@','@','@'],
                                                ['@','.','.','.','@'],
                                                ['@','.','.','.','@'],
                                                ['@','.','.','.','@'],
                                                ['@','@','@','@','@']])

    def test_euclidean_correct_value(self):
        start = (1,1)
        end = (5,4)
        self.assertEqual(self.test_core.euclidean(start,end), 5)
    
    def test_euclidean_incorrect(self):
        start = (1,1)
        end = (5,4)
        self.assertNotEqual(self.test_core.euclidean(start,end), 5.1)        
    
    def test_manhattan_correct_value(self):
        start = (1,1)
        end = (5,4)
        self.assertEqual(self.test_core.manhattan(start,end), 7)

    def test_manhattan_incorrect(self):
        start = (1,1)
        end = (5,4)
        self.assertNotEqual(self.test_core.manhattan(start,end), 7.1)
    
    def test_diagonal_correct_value(self):
        start = (1,1)
        end = (3,4)
        self.assertEqual(round(self.test_core.diagonal(start,end),3), 3.828)

    def test_diagonal_incorrect_(self):
        start = (1,1)
        end = (3,4)
        self.assertNotEqual(self.test_core.diagonal(start,end), 3.828)
    
    def test_path_correct(self):
        start = (1,1)
        end = (3,4)
        parent = {(1,1): None, (2,1): (1,1), (2,3): (2,1), (3,4): (2,3)}
        self.assertEqual(self.test_core.get_path(end, parent),[(1,1),(2,1),(2,3),(3,4)])
    
    def test_path_start_point_missing(self):
        start = (0,1)
        end = (3,4)
        parent = {(1,1): None, (2,1): (0,1), (2,3): (2,1), (3,4): (2,3)}
        self.assertRaises(KeyError, lambda: self.test_core.get_path(end, parent))        

