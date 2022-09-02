import unittest
import sys

sys.path.insert(0, '/Users/pshepper/Developer/Python/Data-Structures')

from SingleLinkedList import SingleLinkedList

class TestSingleLinkedList(unittest.TestCase):

    def test_init(self):
        list = SingleLinkedList()
        
        # Checks list is empty
        self.assertIsNone(list.head)
    
    def test_insert_head(self):
        list = SingleLinkedList()
        list.insert_head(3)

        # 3(H) -> None
        self.assertEqual(list.head.data, 3)
        self.assertIsNone(list.head.next)

        # 2(H) -> 3 -> None
        list.insert_head(2)
        self.assertEqual(list.head.data, 2)
        self.assertEqual(list.head.next.data, 3)

        # 1(H) -> 2 -> 3 -> None
        list.insert_head(1)
        self.assertEqual(list.head.data, 1)
        self.assertEqual(list.head.next.data, 2)
        self.assertEqual(list.head.next.next.data, 3)
        self.assertIsNone(list.head.next.next.next)

    def test_remove_head(self):
        list = SingleLinkedList()
        list.insert_head(3)
        list.insert_head(2)
        list.insert_head(1)

        list.remove_head()

        # 2(H) -> 3 -> None
        self.assertEqual(list.head.data, 2)
        self.assertEqual(list.head.next.data, 3)
        self.assertIsNone(list.head.next.next)

    def test_length(self):
        list = SingleLinkedList()
        list.insert_head(1)
        list.insert_head(2)
        list.insert_head(3)
        list.insert_head(4)

        # 4(H) -> 3 -> 2 -> 1
        self.assertEqual(list.length(), 4)

        list.remove_head()
        list.remove_head()
        list.remove_head()

        # 1(H) -> None
        self.assertEqual(list.length(), 1)

        list.remove_head()

        # Empty list
        self.assertEqual(list.length(), 0)

    def test_index(self):
        list = SingleLinkedList()
        list.insert_head(1)
        list.insert_head(2)
        list.insert_head(3)
        list.insert_head(4)

        # 4(H) -> 3 -> 2 -> 1
        self.assertEqual(list.index(4), 0)
        self.assertEqual(list.index(3), 1)
        self.assertEqual(list.index(1), 3)
    
    def test_insert_index(self):
        list = SingleLinkedList()
        list.insert_head(1)
        list.insert_head(3)
        list.insert_head(4)
        # 4(H) -> 3 -> 1

        list.insert_index(2,2)

       
        # 4(H) -> 3 -> 2 -> 1
        self.assertEqual(list.index(2), 2)
        self.assertEqual(list.head.next.next.data, 2)

    def test_remove_index(self):
        list = SingleLinkedList()
        list.insert_head(1)
        list.insert_head(2)
        list.insert_head(3)
        list.insert_head(4)
        # 4(H) -> 3 -> 2 -> 1

        list.remove_index(2)
        # 4(H) -> 3 -> 1
        self.assertEqual(list.index(3), 1)
        self.assertEqual(list.head.next.next.data, 1)



if __name__ == "__main__":
    unittest.main()
