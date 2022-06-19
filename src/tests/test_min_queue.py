import unittest
from min_queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_empty_list(self):
        self.assertIsInstance(self.queue.queue, list)

    def test_add_to_list(self):
        self.queue.add_to_queue(((5,5),2))
        self.assertEqual(self.queue.queue[0],(2, (5,5)))
    
    def test_add_to_list_value_order(self):
        self.queue.add_to_queue(((1,3),5))
        self.queue.add_to_queue(((4,5),2))
        self.assertEqual(self.queue.queue, [(2, (4,5)), (5, (1,3))])

    def test_clear_list(self):
        self.queue.add_to_queue(((5,5),2))
        self.queue.clear_queue()
        self.assertEqual(self.queue.queue, [])

    def test_remove_min_value(self):
        self.queue.add_to_queue(((2,5),27))
        self.queue.add_to_queue(((1,3),5))
        self.queue.add_to_queue(((4,5),2))
        self.assertEqual(self.queue.remove_from_queue(), ((4,5),2))        
    
    def test_remove_wrong_value(self):
        self.queue.add_to_queue(((2,5),2))
        self.queue.add_to_queue(((1,3),5))
        self.queue.add_to_queue(((4,5),27))
        self.assertNotEqual(self.queue.remove_from_queue(), ((1,3),5))
    
    def test_get_queue(self):
        self.queue.add_to_queue(((5,5),2))
        self.queue.add_to_queue(((1,3),5))
        self.assertEqual(self.queue.get_queue(), [(2,(5,5)),(5, (1,3))])
    
    def test_queue_is_not_empty(self):
        self.queue.add_to_queue(((5,5),2))
        self.queue.add_to_queue(((1,3),5))
        self.assertEqual(self.queue.is_empty(), False)
    
    def test_queue_is_empty(self):
        self.assertNotEqual(self.queue.is_empty(), False)
