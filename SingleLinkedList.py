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
                temp = temp.next
    
if __name__ == "__main__":
    list = SingleLinkedList()
            