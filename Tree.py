# Want to keep data similar to graph.
# A tree is made up of verticies with a single root


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def addChild(self, child):
        '''Add child to node, cannot be self'''
        if isinstance(child, Vertex) and child != self and child.parent == None:
            self.children.append(child.name)
            child.parent = self

    def isLeaf(self):
        if self.children != [] and self.parent != None:
            return True
        else: 
            return False
        
class Tree(object):
    def __init__(self):
        self.verticies = {} # Name <String> : Children [<Strings>]

    def addVertex(self, v1):
        if isinstance(v1, Vertex):
            self.verticies[v1.name] = v1.children

    def deleteSubtree(self, v1):
        '''Removes subtree with v1 as root of tree'''
        return 'foo'

if __name__ == "__main__":
    root = Vertex('r')
    c1 = Vertex('child1')
    c2 = Vertex('child2')
    c11 = Vertex('child11')

    root.addChild(c1)
    print(root.children)
    print(c1.parent.name)

    root.addChild(c2)
    print(root.children)

    c1.addChild(c11)
    print(c1.children)
    print(c11.parent.name)
