class Node(object):
    def __init__(self, data, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def destroyList(self):
        self.head = None
        self.tail = None

    def insertHead(self, data):
        newNode = Node(data)

        if self.head == None and self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode

    def insertTail(self, data):
        newNode = Node(data)

        if self.head == None and self.tail == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
    
    def insertIndex(self, data, index):
        newNode = Node(data)

    def deleteHead(self):
        if self.head == None:
            return -1
        elif self.head == self.tail:
            self.destroyList()
        else:
            temp = self.head

            self.head.next.previous = None
            self.head = self.head.next
            temp.next = None

        
    
    def deleteTail(self, index):
        temp = self.tail

    def deleteIndex(self, index):
        temp = self.head

    def contains(self, data):
        temp = self.head

    def length(self):
        temp = self.head

    def print(self):
        if self.head == None and self.tail == None:
            print("No list")
        else:
            temp = self.head
            while(temp != None):
                print(temp.data, end=" ")
                temp = temp.next


if __name__ == "__main__":
    list = DoublyLinkedList()
    list.print()

    list.insertHead(2)
    list.deleteHead()

    list.print()

    list.insertTail(5)
    list.insertHead(4)
    list.insertTail(6)
    list.deleteHead()

    list.print()