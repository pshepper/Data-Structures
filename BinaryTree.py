# Class for node
class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 
        # parent

    def addLeft(self, vertex):
        if isinstance(vertex, Vertex) and self.left == None:
            self.left = vertex

    def addRight(self, vertex):
        if isinstance(vertex, Vertex) and self.right == None:
            self.right = vertex

class Tree(object):
    def __init__(self) -> None:
        self.root = None

    # Takes value and root of tree/subtree
    def addVertex(self, value, root=None):
        if root == None:
            root = self.root
    
        if self.root == None:
            self.root = Vertex(value)
        else:
            if value <= root.value:
                if root.left == None:
                    root.left == Vertex(value)
                    # parent
                else:
                    return self.addVertex(value, root= root.left)
            if value < root.key:
                if root.right == None:
                    root.right == Vertex(value)
                    # parent
                else:
                    return self.addVertex(value, root= root.right)

    def search(self, value, root=None):
        x = 1

    def deleteVertex(self, value, node=None):
        x = 1
        

        




