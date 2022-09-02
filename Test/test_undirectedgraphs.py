import unittest
import sys

sys.path.insert(0, '/Users/pshepper/Developer/Python/Data-Structures')

from UndirectedGraph import Graph, Vertex

class TestUndirectedGraph(unittest.TestCase):

    def test_init(self):
        graph = Graph()

    def test_add_vertex(self):
        graph = Graph()
        v1 = Vertex('v1')
        v2 = Vertex('v2')

        graph.add_vertex(v1)
        graph.add_vertex(v2)
        self.assertIn('v1', graph.verticies)
        self.assertIn('v2', graph.verticies)

    def test_remove_vertex(self):
        graph = Graph()

        v1 = Vertex('v1')
        v2 = Vertex('v2')

        graph.add_vertex(v1)
        graph.add_vertex(v2)
        self.assertIn('v1', graph.verticies)

        graph.remove_vertex(v1)

        self.assertIn('v2', graph.verticies)
        self.assertNotIn('v1', graph.verticies)

    def test_edges(self):
        graph = Graph()

        v1 = Vertex('v1')
        v2 = Vertex('v2')
        v3 = Vertex('v3')

        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_vertex(v3)

        graph.add_edge(v1, v2)
        self.assertEqual(['v2'], graph.verticies['v1'])
        self.assertEqual(['v1'], graph.verticies['v2'])

        graph.add_edge(v1, v3)
        self.assertEqual(['v2', 'v3'], graph.verticies['v1'])
        # Ordering

        

if __name__ == "__main__":
    unittest.main()

        
