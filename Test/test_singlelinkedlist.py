import unittest
import sys

sys.path.insert(0, '/Users/pshepper/Developer/Python/Data-Structures')

from SingleLinkedList import SingleLinkedList

class TestSingleLinkedList(unittest.TestCase):

    def test_init(self):
        list = SingleLinkedList()
        
        self.assertIsNone(list.head)
    
    def test_insertHead(self):
        list = SingleLinkedList()
        list.insertHead(3)

        self.assertEqual(list.head.data, 3)
        self.assertIsNone(list.head.next)

        list.insertHead(2)
        self.assertEqual(list.head.data, 2)
        self.assertEqual(list.head.next.data, 3)
    
if __name__ == "__main__":
    unittest.main()
