import unittest
from prim import prim


class PrimTests(unittest.TestCase):

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
        expected = {'A': 0, 'B': 4, 'C': 2, 'D': 1, 'E': 1, 'F': 8, 'G': 11} 

        self.assertEqual(prim(graph, source), expected)

    def test2(self):
        graph = {
            'U': [('V', 2), ('W', 5), ('X', 1)],
            'V': [('U', 2), ('X', 2), ('W', 3)],
            'W': [('V', 3), ('U', 5), ('X', 3), ('Y', 1), ('Z', 5)],
            'X': [('U', 1), ('V', 2), ('W', 3), ('Y', 1)],
            'Y': [('X', 1), ('W', 1), ('Z', 1)],
            'Z': [('W', 5), ('Y', 1)],
        }

        source = 'U'
        expected = {'U': 0, 'V': 2, 'W': 1, 'X': 1, 'Y': 1, 'Z': 1}

        self.assertEqual(prim(graph, source), expected)


if __name__ == '__main__':
    unittest.main()
