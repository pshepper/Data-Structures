import unittest
import sys

sys.path.insert(0, '/Users/pshepper/Developer/Python/Data-Structures')

from UndirectedGraph import Graph, Vertex

class TestUndirectedGraph(unittest.TestCase):

    def test_init(self):
        graph = Graph()

    def test_addVertex(self):
        graph = Graph()
        v1 = Vertex('v1')
        v2 = Vertex('v2')

        graph.addVertex(v1)
        graph.addVertex(v2)
        self.assertIn('v1', graph.verticies)
        self.assertIn('v2', graph.verticies)

    def test_deleteVertex(self):
        graph = Graph()

        v1 = Vertex('v1')
        v2 = Vertex('v2')

        graph.addVertex(v1)
        graph.addVertex(v2)
        self.assertIn('v1', graph.verticies)

        graph.deleteVertex(v1)

        self.assertIn('v2', graph.verticies)
        self.assertNotIn('v1', graph.verticies)

    def test_edges(self):
        graph = Graph()

        v1 = Vertex('v1')
        v2 = Vertex('v2')
        v3 = Vertex('v3')

        graph.addVertex(v1)
        graph.addVertex(v2)
        graph.addVertex(v3)

        graph.addEdge(v1, v2)
        self.assertEqual(['v2'], graph.verticies['v1'])
        self.assertEqual(['v1'], graph.verticies['v2'])

        graph.addEdge(v1, v3)
        self.assertEqual(['v2', 'v3'], graph.verticies['v1'])
        # Ordering

        

if __name__ == "__main__":
    unittest.main()

        
