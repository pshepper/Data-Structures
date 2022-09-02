# Class for node
class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 
        # parent

    def add_left(self, vertex):
        if isinstance(vertex, Vertex) and self.left == None:
            self.left = vertex

    def add_right(self, vertex):
        if isinstance(vertex, Vertex) and self.right == None:
            self.right = vertex

class Tree(object):
    def __init__(self) -> None:
        self.root = None

    # Takes value and root of tree/subtree
    def add_vertex(self, value, root=None):
        
        if self.root == None:
            self.root = Vertex(value)
            return
        if root == None:
            root = self.root
        # else:
        if value <= root.value:
            if root.left == None:
                root.left = Vertex(value) 
                # parent
            else:
                return self.add_vertex(value, root= root.left)
        if value > root.value:
            if root.right == None:
                root.right = Vertex(value)
                # parent
            else:
                return self.add_vertex(value, root= root.right)

    def search(self, value, root=None):
        if root == None:
            root = self.root
        if self.root.value == value:
            return self.root
        else:
            if root.value == value:
                return root
            elif value < root.value:
                return self.search(value, root=root.left)
            elif value > root.value:
                return self.search(value, root=root.right)

    def remove_vertex(self, value, node=None):
        x = 1
        
if __name__ == "__main__":
    tree = Tree()

    tree.add_vertex(10)
    tree.add_vertex(5)
    tree.add_vertex(15)

    root = tree.root
    print(root.value)
    print(root.left.value)
    print(root.right.value)

    print(tree.search(5))



