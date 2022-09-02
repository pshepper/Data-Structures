# Want to keep data similar to graph.
# A tree is made up of verticies with a single root



class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self, child):
        '''Add child to node, cannot be self'''
        if isinstance(child, Vertex) and child != self and child.parent == None:
            self.children.append(child.name)
            child.parent = self

    def remove_child(self, child):
        if isinstance(child, Vertex) and child.name in self.children:
            self.children.remove(child.name)

    def is_leaf(self):
        if self.children == [] and self.parent != None:
            return True
        else: 
            return False
        
class Tree(object):
    def __init__(self):
        self.verticies = {} # Name <String> : Children [<Strings>]

    def add_vertex(self, v):
        if isinstance(v, Vertex):
            self.verticies[v.name] = v.children

if __name__ == "__main__":
    root = Vertex('r')
    c1 = Vertex('child1')
    c2 = Vertex('child2')
    c11 = Vertex('child11')

    root.add_child(c1)
    print(root.children)
    print(c1.parent.name)

    root.add_child(c2)
    print(root.children)

    c1.add_child(c11)
    print(c1.children)
    print(c11.parent.name)

    tree = Tree()
    tree.add_vertex(root)
    tree.add_vertex(c1)
    tree.add_vertex(c2)
    tree.add_vertex(c11)
    print(tree.verticies)

    root.remove_child(c1)
    print(tree.verticies)
    print(root.children)
