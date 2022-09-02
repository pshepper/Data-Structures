import unittest
import sys

sys.path.insert(0, '/Users/pshepper/Developer/Python/Data-Structures')

from DoublyLinkedList import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):

    def test_init(self):
        dList = DoublyLinkedList()

        # Checks list exist with empty head and tail pointer
        self.assertIsNone(dList.head, dList.tail)

    def test_insert_head(self):
        dList = DoublyLinkedList()
        
        dList.insert_head(3)

        # 3(H) <-> None
        self.assertEqual(dList.head.data, 3)
        self.assertIsNone(dList.head.next)

        # 2(H) <-> 3 <-> None
        dList.insert_head(2)
        self.assertEqual(dList.head.data, 2)
        self.assertEqual(dList.head.next.data, 3)

        # 1(H) <-> 2 <-> 3 <-> None
        dList.insert_head(1)
        self.assertEqual(dList.head.data, 1)
        self.assertEqual(dList.head.next.data, 2)
        self.assertEqual(dList.head.next.next.data, 3)
        self.assertIsNone(dList.head.next.next.next)

    def test_insert_tail(self):
        dList = DoublyLinkedList()

        dList.insert_tail(1)

        # 1 (H&T) -> None
        self.assertEqual(dList.tail, dList.head)
        self.assertEqual(dList.tail.data, 1)

        dList.insert_tail(2)

        # 1(H) <-> 2(T) -> None
        self.assertNotEqual(dList.tail, dList.head)
        self.assertEqual(dList.head.data, 1)
        self.assertEqual(dList.tail.data, 2)
        self.assertEqual(dList.tail.previous.data, 1)

        dList.insert_head(0)

        # 0(H) <-> 1 <-> 2(T) -> None
        self.assertEqual(dList.head.data, 0)
        self.assertEqual(dList.head.next.data, 1)
        self.assertEqual(dList.head.next.previous.data, 0)
        self.assertEqual(dList.tail.previous.data, 1)

    def test_remove_head(self):
        dList = DoublyLinkedList()

        dList.insert_head(3)
        dList.insert_head(2)
        dList.insert_head(1)
        dList.insert_head(0)
        # 0(H) <-> 1 <-> 2 <-> 3 -> None

        dList.remove_head()

        # 1(H) <-> 2 <-> 3 -> None
        self.assertEqual(dList.head.data, 1)
        self.assertEqual(dList.tail.data, 3)
        self.assertEqual(dList.head.next.data, 2)
        self.assertEqual(dList.head.next.previous.data, 1)

        dList.remove_head()
        dList.remove_head()

        # 3(H&T) -> None
        self.assertEqual(dList.head.data, 3)
        self.assertIsNone(dList.head.next)

        dList.remove_head()

        # Empty list
        self.assertIsNone(dList.head, dList.tail)

    def test_remove_tail(self):
        dList = DoublyLinkedList()

        dList.insert_head(3)
        dList.insert_head(2)
        dList.insert_head(1)

        dList.remove_tail()

        # 1(H) <-> 2(T) <-> None
        self.assertEqual(dList.head.data, 1)
        self.assertEqual(dList.tail.data, 2)
        self.assertIsNone(dList.tail.next)
        self.assertEqual(dList.tail.previous.data, 1)

    def test_length(self):
        dList = DoublyLinkedList()

        # Empty list
        self.assertIsNone(dList.head, dList.tail)
        self.assertEqual(dList.length(), 0)

        dList.insert_head(1)
        dList.insert_tail(2)

        # 1(H) <-> 2(T)
        self.assertEqual(dList.length(), 2)

        dList.insert_head(0)

        # 0(H) <-> 1 <-> 2(T)
        self.assertEqual(dList.length(), 3)

        dList.remove_head()

        # 1(H) <-> 2(T)
        self.assertEqual(dList.length(), 2)

    def test_index(self):
        dList = DoublyLinkedList()

        dList.insert_head(1)
        dList.insert_head(2)
        dList.insert_head(3)
        dList.insert_head(4)

        # 4(H) -> 3 -> 2 -> 1
        self.assertEqual(dList.index(4), 0)
        self.assertEqual(dList.index(3), 1)
        self.assertEqual(dList.index(1), 3)

    def test_insert_index(self):
        dList = DoublyLinkedList()

        dList.insert_head(1)
        dList.insert_head(3)
        dList.insert_head(4)
        # 4(H) <-> 3 <-> 1(T) <-> None

        dList.insert_index(2,2)

        # 4(H) <-> 3 <-> 2 <-> 1(T) <-> None
        self.assertEqual(dList.index(2), 2)
        self.assertEqual(dList.head.next.next.data, 2)
        self.assertEqual(dList.tail.previous.next.data, 1)
        self.assertEqual(dList.tail.previous.data, 2)

    def test_remove_index(self):
        dList = DoublyLinkedList()

        dList.insert_head(1)
        dList.insert_head(2)
        dList.insert_head(3)
        dList.insert_head(4)
        # 4(H) <-> 3 <-> 2 <-> 1

        dList.remove_index(2)

        # 4(H) <-> 3 <-> 1
        self.assertEqual(dList.index(3), 1)
        self.assertEqual(dList.index(1), 2)
        self.assertEqual(dList.head.next.next.data, 1)
        self.assertEqual(dList.tail.previous.next.data, 1)
        self.assertEqual(dList.tail.data, 1)



if __name__ == "__main__":
    unittest.main()