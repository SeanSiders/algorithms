import unittest
from merge_sort import sort


class MergeSortTests(unittest.TestCase):

    def test1(self):

        source = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]

        sort(source)
        self.assertEqual(source, expected)


    def test2(self):

        source = [80, 2.2, 55, 103, 0.0, .0005, 890, 10000, 7]
        expected = [0.0, .0005, 2.2, 7, 55, 80, 103, 890, 10000]

        sort(source)
        self.assertEqual(source, expected)


    def test3(self):

        source = [4, 0, 400, 50, 2, 4000, -2, -4000, 8999]
        expected = [-4000, -2, 0, 2, 4, 50, 400, 4000, 8999]

        sort(source)
        self.assertEqual(source, expected)


    def test4(self):

        source = [1]
        expected = [1]

        sort(source)
        self.assertEqual(source, expected)


    def test5(self):

        source = []
        expected = []

        sort(source)
        self.assertEqual(source, expected)


    def test6(self):

        source = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

        sort(source)
        self.assertEqual(source, expected)


    def test7(self):

        source = [2, 0, 0, 0, 0, 0, 0, -4, 0, 0, 0, 0, 0, 0, 0, 1]
        expected = [-4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2]

        sort(source)
        self.assertEqual(source, expected)


if __name__ == '__main__':
    unittest.main()
