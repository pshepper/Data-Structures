# Vertex object has name and array of neighbors
# TODO: find ways to specify error type

from tabnanny import verbose


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def addNeighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor not in self.neighbors:
                self.neighbors.append(neighbor.name)
                neighbor.neighbors.append(self.name)
            else:
                return -1 
        else: 
            return -1

    def deleteNeighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.name in self.neighbors:
                self.neighbors.remove(neighbor.name)
                neighbor.neighbors.remove(self.name)


class Graph(object):
    def __init__(self):
        self.verticies = {} # Name : Neighbors 

    def addVertex(self, v1):
        self.verticies[v1.name] = v1.neighbors

    def addEdge(self, v1, v2):
        # Check if verticies on graph
        if v1.name and v2.name in self.verticies:
            if isinstance(v1, Vertex) and isinstance(v2, Vertex):
                v1.addNeighbor(v2)

    def deleteVertex(self, v1):
        '''Unattaches all edges of vertex v1 and removes it from graph'''
        if v1.name in self.verticies:
            if isinstance(v1, Vertex):
                for n in v1.neighbors:
                    v1.deleteNeighbor(n)
                self.verticies.pop(v1.name)

    def deleteEdge(self, v1, v2):
        if v1.name and v2.name in self.verticies:
            if isinstance(v1, Vertex) and isinstance(v2, Vertex):
                v1.deleteNeighbor(v2)

    def printAdjencyList(self):
            # Will want to sort graph before
            list = ["{} : {}".format(vertex, self.verticies[vertex]) for vertex in self.verticies]
            for vertex in list:
                print(vertex)
            #str(vertex) + ":" + str(self.verticies[vertex.name])

if __name__ == "__main__":
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')

    graph = Graph()
    

    graph.addVertex(a)
    graph.addVertex(b)
    graph.addVertex(c)
    graph.addEdge(a, b)
    graph.addEdge(b, c)

    d = Vertex('d')
    graph.addVertex(d)
    graph.addEdge(a, d)

    
    a.deleteNeighbor(b)
    a.addNeighbor(b)

    #print(graph.verticies)
    print(graph.printAdjencyList())

    x =1