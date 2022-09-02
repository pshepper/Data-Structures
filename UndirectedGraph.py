# Vertex object has name and array of neighbors
# TODO: find ways to specify error type


class Vertex(object):
    def __init__(self, name):
        # Check if name is string
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor not in self.neighbors:
                self.neighbors.append(neighbor.name)
                neighbor.neighbors.append(self.name)
            else:
                return -1 
        else: 
            return -1

    def remove_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.name in self.neighbors:
                self.neighbors.remove(neighbor.name)
                neighbor.neighbors.remove(self.name)


class Graph(object):
    def __init__(self):
        self.verticies = {} # Name : Neighbors 

    def add_vertex(self, v1):
        self.verticies[v1.name] = v1.neighbors

    def add_edge(self, v1, v2):
        # Check if verticies on graph
        if v1.name and v2.name in self.verticies:
            if isinstance(v1, Vertex) and isinstance(v2, Vertex):
                v1.add_neighbor(v2)

    def remove_vertex(self, v1):
        '''Unattaches all edges of vertex v1 and removes it from graph'''
        if v1.name in self.verticies:
            if isinstance(v1, Vertex):
                for n in v1.neighbors:
                    v1.remove_neighbor(n)
                self.verticies.pop(v1.name)

    def remove_edge(self, v1, v2):
        if v1.name and v2.name in self.verticies:
            if isinstance(v1, Vertex) and isinstance(v2, Vertex):
                v1.remove_neighbor(v2)

    def adjaceny_list(self):
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
    

    graph.add_vertex(a)
    graph.add_vertex(b)
    graph.add_vertex(c)
    graph.add_edge(a, b)
    graph.add_edge(b, c)

    d = Vertex('d')
    graph.add_vertex(d)
    graph.add_edge(a, d)

    
    a.remove_neighbor(b)
    a.add_neighbor(b)

    #print(graph.verticies)
    print(graph.adjaceny_list())

    x =1