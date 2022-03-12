import unittest
from topological_sort import topologicalSort_BFS, topologicalSort_DFS


class TopSortTests(unittest.TestCase):
    def test1(self):
        graph = {
            'A': ['B', 'C', 'D'],
            'B': ['D', 'E', 'F'],
            'C': ['F', 'G'],
            'D': ['F', 'G'],
            'E': [],
            'F': ['G'],
            'G': []
        }

        source = 'A'

        expected_BFS = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] 
        expected_DFS = ['A', 'B', 'D', 'F', 'G', 'E', 'C']

        self.assertEqual(topologicalSort_BFS(graph, source), expected_BFS)
        self.assertEqual(topologicalSort_DFS(graph, source), expected_DFS)


    def test2(self):
        graph = {
            'A': ['B'],
            'B': ['C'],
            'C': ['D'],
            'D': ['E'],
            'E': ['F'],
            'F': ['G'],
            'G': []
        }

        source = 'A'

        expected_BFS = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] 
        expected_DFS = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] 

        self.assertEqual(topologicalSort_BFS(graph, source), expected_BFS)
        self.assertEqual(topologicalSort_DFS(graph, source), expected_DFS)


    def test3(self):
        graph = {
            'A': ['C'],
            'B': ['F', 'G'],
            'C': ['B', 'E', 'F', 'G'],
            'D': [],
            'E': [],
            'F': [],
            'G': []
        }

        source = 'A'

        expected_BFS = ['A', 'C', 'B', 'E', 'F', 'G'] 
        expected_DFS = ['A', 'C', 'B', 'F', 'G', 'E']

        self.assertEqual(topologicalSort_BFS(graph, source), expected_BFS)
        self.assertEqual(topologicalSort_DFS(graph, source), expected_DFS)

    def test4(self):
        graph = {
            'A': ['C', 'E', 'F', 'G', 'I'],
            'B': ['E', 'G', 'H', 'J'],
            'C': ['B', 'D', 'H', 'I', 'J'],
            'D': ['E'],
            'E': ['H', 'J'],
            'F': ['I'],
            'G': ['H', 'I'],
            'H': [],
            'I': [],
            'J': []
        }

        source = 'A'

        expected_BFS = ['A', 'C', 'E', 'F', 'G', 'I', 'B', 'D', 'H', 'J'] 
        expected_DFS = ['A', 'C', 'B', 'E', 'H', 'J', 'G', 'I', 'D', 'F']

        self.assertEqual(topologicalSort_BFS(graph, source), expected_BFS)
        self.assertEqual(topologicalSort_DFS(graph, source), expected_DFS)


if __name__ == '__main__':
    unittest.main()
