# Directed Graphs will have the same information as undirected graphs
# but a neighbor is only a vertex that can be reached from a current vertex

# NOTE: Going to be a bit bare bones. Will add graph related algorithms later

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.neighbors = [] # [<Strings>]

    def addNeighbor(self,neighbor):
        '''neighbors are only verticies that can be reached'''
        if isinstance(neighbor, Vertex):
            if neighbor not in self.neighbors:
                self.neighbors.append(neighbor.name)
            else:
                return -1
        else: 
            return -1

# For now choosing to not have addEdge function
# Want only 1 way to add connection, having it by a function of the vertex object
# makes it more clear the direction of the edge

class Graph(object):
    def __init__(self):
        self.verticies = {} # Name<String> : Neighbors [<Strings>]

    def addVertex(self, v1):
        if isinstance(v1, Vertex):
            self.verticies[v1.name] = v1.neighbors