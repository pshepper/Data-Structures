import unittest
import sys

sys.path.insert(0, '/Users/pshepper/Developer/Python/Data-Structures')

from SingleLinkedList import SingleLinkedList

class TestSingleLinkedList(unittest.TestCase):

    def test_init(self):
        list = SingleLinkedList()
        
        # Checks list is empty
        self.assertIsNone(list.head)
    
    def test_insertHead(self):
        list = SingleLinkedList()
        list.insertHead(3)

        # 3(H) -> None
        self.assertEqual(list.head.data, 3)
        self.assertIsNone(list.head.next)

        # 2(H) -> 3 -> None
        list.insertHead(2)
        self.assertEqual(list.head.data, 2)
        self.assertEqual(list.head.next.data, 3)

        # 1(H) -> 2 -> 3 -> None
        list.insertHead(1)
        self.assertEqual(list.head.data, 1)
        self.assertEqual(list.head.next.data, 2)
        self.assertEqual(list.head.next.next.data, 3)
        self.assertIsNone(list.head.next.next.next)

    def test_deleteHead(self):
        list = SingleLinkedList()
        list.insertHead(3)
        list.insertHead(2)
        list.insertHead(1)

        list.deleteHead()

        # 2(H) -> 3 -> None
        self.assertEqual(list.head.data, 2)
        self.assertEqual(list.head.next.data, 3)
        self.assertIsNone(list.head.next.next)

    def test_length(self):
        list = SingleLinkedList()
        list.insertHead(1)
        list.insertHead(2)
        list.insertHead(3)
        list.insertHead(4)

        # 4(H) -> 3 -> 2 -> 1
        self.assertEqual(list.length(), 4)

        list.deleteHead()
        list.deleteHead()
        list.deleteHead()

        # 1(H) -> None
        self.assertEqual(list.length(), 1)

        list.deleteHead()

        # Empty list
        self.assertEqual(list.length(), 0)

    def test_index(self):
        list = SingleLinkedList()
        list.insertHead(1)
        list.insertHead(2)
        list.insertHead(3)
        list.insertHead(4)

        # 4(H) -> 3 -> 2 -> 1
        self.assertEqual(list.index(4), 0)
        self.assertEqual(list.index(3), 1)
        self.assertEqual(list.index(1), 3)
    
    def test_insertIndex(self):
        list = SingleLinkedList()
        list.insertHead(1)
        list.insertHead(3)
        list.insertHead(4)
        # 4(H) -> 3 -> 1

        list.insertIndex(2,2)

       
        # 4(H) -> 3 -> 2 -> 1
        self.assertEqual(list.index(2), 2)
        self.assertEqual(list.head.next.next.data, 2)

    def test_deleteIndex(self):
        list = SingleLinkedList()
        list.insertHead(1)
        list.insertHead(2)
        list.insertHead(3)
        list.insertHead(4)
        # 4(H) -> 3 -> 2 -> 1

        list.deleteIndex(2)

        # 4(H) -> 3 -> 1
        self.assertEqual(list.index(1), 2)
        self.assertEqual(list.head.next.next.data, 1)



if __name__ == "__main__":
    unittest.main()
