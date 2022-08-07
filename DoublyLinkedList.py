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
        temp = self.head

        if index == 0:
            self.insertHead(data)
        else: 
            while index != 0:
                temp = temp.next
                index -= 1

            newNode.next = temp
            newNode.previous = temp.previous
            newNode.previous.next = newNode
            temp.previous = newNode

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

    def deleteTail(self):
        if self.tail == None:
            return -1
        elif self.tail == self.head:
            self.destroyList()
        else:
            temp = self.tail.previous
            temp.next = None
            self.tail.previous = None
            self.tail = temp

    def deleteIndex(self, index):
        temp = self.head

        if index == 0:
            self.deleteHead()
        elif index == self.length() - 1:
            self.deleteTail
        else:
            while index != 0:
                temp = temp.next
                index -= 1
            temp.next.previous = temp.previous
            temp.previous.next = temp.next
            temp.next = None
            temp.previous = None

    def index(self, data):
        '''Returns first index of data that is within a list'''
        temp = self.head
        index = 0
        if self.head.data == data:
            return index
        while temp.next != None:
            temp = temp.next
            index += 1
            if temp.data == data:
                return index
        return None

    def contains(self, data):
        temp = self.head
        while temp.next != None:
            if temp.data == data:
                return True
            temp = temp.next
        return False


    def length(self):
        if self.tail == None and self.head == None:
            return 0

        temp = self.head
        length = 1
        
        while temp.next != None:
            length += 1
            temp = temp.next
        return length


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