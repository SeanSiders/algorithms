import unittest
from dijkstra import dijkstra


class DijkstraTests(unittest.TestCase):

    def test1(self):
        graph = {
            'A': [('B', 11), ('C', 2), ('D', 1)],
            'B': [('D', 4), ('E', 1), ('F', 9)],
            'C': [('F', 16), ('G', 12)],
            'D': [('B', 4), ('F', 8), ('G', 11)],
            'E': [],
            'F': [('G', 11)],
            'G': []
        }

        source = 'A'
        expected = {'A': 0, 'B': 5, 'C': 2, 'D': 1, 'E': 6, 'F': 9, 'G': 12} 

        self.assertEqual(dijkstra(graph, source), expected)

    def test2(self):
        graph = {
            'U': [('V', 2), ('W', 5), ('X', 1)],
            'V': [('U', 2), ('X', 2), ('W', 3)],
            'W': [('V', 3), ('U', 5), ('X', 3), ('Y', 1), ('Z', 5)],
            'X': [('U', 1), ('V', 2), ('W', 3), ('Y', 1)],
            'Y': [('X', 1), ('W', 1), ('Z', 1)],
            'Z': [('W', 5), ('Y', 1)],
        }

        source = 'X'
        expected = {'U': 1, 'V': 2, 'W': 2, 'X': 0, 'Y': 1, 'Z': 2}

        self.assertEqual(dijkstra(graph, source), expected)
    
    def test3(self):
        graph = {
            'A': [('D', 4), ('B', 15)],
            'B': [('E', 4), ('G', 2)],
            'C': [('F', 1), ('G', 1)],
            'D': [('C', 0), ('G', 3)],
            'E': [('F', 7)],
            'F': [('G', 9), ('E', 7)],
            'G': [('B', 2), ('E', 18)]
        }

        source = 'A'
        expected = {'A': 0, 'D': 4, 'B': 7, 'G': 5, 'C': 4, 'F': 5, 'E': 11}

        self.assertEqual(dijkstra(graph, source), expected)


if __name__ == '__main__':
    unittest.main()
