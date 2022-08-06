class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def destroyList(self):
        self.head = None

    def insertHead(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertIndex(self, data, index):
        newNode = Node(data)
        temp = self.head
        previousNode = None

        if index == 0:
            self.insertHead(data)
        else: 
            while index != 0:
                previousNode = temp
                temp = temp.next
                index -= 1
            previousNode.next = newNode
            newNode.next = temp
    
    def deleteHead(self):
        if self.head == None:
            return -1
        elif self.length == 1:
            self.destroyList()
        else:
            temp = self.head

            self.head = self.head.next
            temp.next = None

    def deleteIndex(self, index):
        temp = self.head
        previousNode = None

        if index == 0:
            self.deleteHead()
        else:
            while index != 0:
                previousNode = temp
                temp = temp.next
                index -= 1
            previousNode.next = temp.next
            temp.next = None

    def index(self, data):
        '''Returns first index of data that is within list'''
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
        if self.head == None:
            return 0
        else:
            temp = self.head
            length = 1

            while temp.next != None:
                length += 1
                temp = temp.next
            return length

            
    def print(self):
        if self.head == None:
            print("No list")
        else: 
            temp = self.head
            while(temp != None):
                print(temp.data, end=" ")
                if(temp.next != None):
                    print("->", end=" ")
                else:
                    print("-> NONE", end="\n")
                temp = temp.next
    
if __name__ == "__main__":
    list = SingleLinkedList()

    list.insertHead(1)
    list.insertHead(2)
    list.insertHead(3)
    list.insertHead(4)

    list.print()

    list.deleteIndex(2)
    list.print()
    
            