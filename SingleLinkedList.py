class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def reset_list(self):
        self.head = None

    def insert_head(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insert_index(self, data, index):
        newNode = Node(data)
        temp = self.head
        previousNode = None

        if index == 0:
            self.insert_head(data)
        else: 
            while index != 0:
                previousNode = temp
                temp = temp.next
                index -= 1
            previousNode.next = newNode
            newNode.next = temp
    
    def remove_head(self):
        if self.head == None:
            return -1
        elif self.length == 1:
            self.reset_list()
        else:
            temp = self.head

            self.head = self.head.next
            temp.next = None

    def remove_index(self, index):
        temp = self.head
        previousNode = None

        if index == 0:
            self.remove_head()
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

    list.insert_head(1)
    list.insert_head(2)
    list.insert_head(3)
    list.insert_head(4)

    list.print()

    list.remove_index(2)
    list.print()
    
            