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

    def test_method_euclidean_correct_value(self):
        start = (1,1)
        end = (5,4)
        self.assertEqual(self.test_core.heuristic_method(start,end, 2), 5)        
    
    def test_method_euclidean_incorrect(self):
        start = (1,1)
        end = (5,4)
        self.assertNotEqual(self.test_core.heuristic_method(start,end, 2), 5.1)        
    
    def test_method_manhattan_correct_value(self):
        start = (1,1)
        end = (5,4)
        self.assertEqual(self.test_core.heuristic_method(start,end,1), 7)

    def test_method_manhattan_incorrect(self):
        start = (1,1)
        end = (5,4)
        self.assertNotEqual(self.test_core.heuristic_method(start,end,1), 7.1)
    
    def test_method_diagonal_correct_value(self):
        start = (1,1)
        end = (3,4)
        self.assertEqual(round(self.test_core.heuristic_method(start,end, 3),3), 3.828)

    def test__method_diagonal_incorrect_(self):
        start = (1,1)
        end = (3,4)
        self.assertNotEqual(self.test_core.heuristic_method(start,end, 3), 3.828)
    
    def test_method_jps(self):
        start = (1,1)
        end = (3,4)
        self.assertEqual(round(self.test_core.heuristic_method(start,end, 0),3), 3.828)        
    
    def test_path_correct(self):
        end = (3,4)
        parent = {(1,1): None, (2,1): (1,1), (2,3): (2,1), (3,4): (2,3)}
        self.assertEqual(self.test_core.get_path(end, parent),[(1,1),(2,1),(2,3),(3,4)])
    
    def test_path_start_point_missing(self):
        end = (3,4)
        parent = {(1,1): None, (2,1): (0,1), (2,3): (2,1), (3,4): (2,3)}
        self.assertRaises(KeyError, lambda: self.test_core.get_path(end, parent))        

