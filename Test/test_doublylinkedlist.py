import unittest
import sys

sys.path.insert(0, '/Users/pshepper/Developer/Python/Data-Structures')

from DoublyLinkedList import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):

    def test_init(self):
        dList = DoublyLinkedList()

        # Checks list exist with empty head and tail pointer
        self.assertIsNone(dList.head, dList.tail)

    def test_insertHead(self):
        dList = DoublyLinkedList()
        
        dList.insertHead(3)

        # 3(H) <-> None
        self.assertEqual(dList.head.data, 3)
        self.assertIsNone(dList.head.next)

        # 2(H) <-> 3 <-> None
        dList.insertHead(2)
        self.assertEqual(dList.head.data, 2)
        self.assertEqual(dList.head.next.data, 3)

        # 1(H) <-> 2 <-> 3 <-> None
        dList.insertHead(1)
        self.assertEqual(dList.head.data, 1)
        self.assertEqual(dList.head.next.data, 2)
        self.assertEqual(dList.head.next.next.data, 3)
        self.assertIsNone(dList.head.next.next.next)

    def test_insertTail(self):
        dList = DoublyLinkedList()

        dList.insertTail(1)

        # 1 (H&T) -> None
        self.assertEqual(dList.tail, dList.head)
        self.assertEqual(dList.tail.data, 1)

        dList.insertTail(2)

        # 1(H) <-> 2(T) -> None
        self.assertNotEqual(dList.tail, dList.head)
        self.assertEqual(dList.head.data, 1)
        self.assertEqual(dList.tail.data, 2)
        self.assertEqual(dList.tail.previous.data, 1)

        dList.insertHead(0)

        # 0(H) <-> 1 <-> 2(T) -> None
        self.assertEqual(dList.head.data, 0)
        self.assertEqual(dList.head.next.data, 1)
        self.assertEqual(dList.head.next.previous.data, 0)
        self.assertEqual(dList.tail.previous.data, 1)

    def test_deleteHead(self):
        dList = DoublyLinkedList()

        dList.insertHead(3)
        dList.insertHead(2)
        dList.insertHead(1)
        dList.insertHead(0)
        # 0(H) <-> 1 <-> 2 <-> 3 -> None

        dList.deleteHead()

        # 1(H) <-> 2 <-> 3 -> None
        self.assertEqual(dList.head.data, 1)
        self.assertEqual(dList.tail.data, 3)
        self.assertEqual(dList.head.next.data, 2)
        self.assertEqual(dList.head.next.previous.data, 1)

        dList.deleteHead()
        dList.deleteHead()

        # 3(H&T) -> None
        self.assertEqual(dList.head.data, 3)
        self.assertIsNone(dList.head.next)

        dList.deleteHead()

        # Empty list
        self.assertIsNone(dList.head, dList.tail)

    def test_deleteTail(self):
        dList = DoublyLinkedList()

        dList.insertHead(3)
        dList.insertHead(2)
        dList.insertHead(1)

        dList.deleteTail()

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

        dList.insertHead(1)
        dList.insertTail(2)

        # 1(H) <-> 2(T)
        self.assertEqual(dList.length(), 2)

        dList.insertHead(0)

        # 0(H) <-> 1 <-> 2(T)
        self.assertEqual(dList.length(), 3)

        dList.deleteHead()

        # 1(H) <-> 2(T)
        self.assertEqual(dList.length(), 2)

    def test_index(self):
        dList = DoublyLinkedList()

        dList.insertHead(1)
        dList.insertHead(2)
        dList.insertHead(3)
        dList.insertHead(4)

        # 4(H) -> 3 -> 2 -> 1
        self.assertEqual(dList.index(4), 0)
        self.assertEqual(dList.index(3), 1)
        self.assertEqual(dList.index(1), 3)

    def test_insertIndex(self):
        dList = DoublyLinkedList()

        dList.insertHead(1)
        dList.insertHead(3)
        dList.insertHead(4)
        # 4(H) <-> 3 <-> 1(T) <-> None

        dList.insertIndex(2,2)

        # 4(H) <-> 3 <-> 2 <-> 1(T) <-> None
        self.assertEqual(dList.index(2), 2)
        self.assertEqual(dList.head.next.next.data, 2)
        self.assertEqual(dList.tail.previous.next.data, 1)
        self.assertEqual(dList.tail.previous.data, 2)

    def test_deleteIndex(self):
        dList = DoublyLinkedList()

        dList.insertHead(1)
        dList.insertHead(2)
        dList.insertHead(3)
        dList.insertHead(4)
        # 4(H) <-> 3 <-> 2 <-> 1

        dList.deleteIndex(2)

        # 4(H) <-> 3 <-> 1
        self.assertEqual(dList.index(3), 1)
        self.assertEqual(dList.index(1), 2)
        self.assertEqual(dList.head.next.next.data, 1)
        self.assertEqual(dList.tail.previous.next.data, 1)
        self.assertEqual(dList.tail.data, 1)



if __name__ == "__main__":
    unittest.main()