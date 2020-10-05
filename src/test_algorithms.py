import unittest
from random import shuffle
from algorithmsv2.selectionsort import test_selection_sort
from algorithmsv2.doubleselectionsort import test_double_selection_sort

class TestAlgorithms(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.array = [i for i in range(20)]
        self.control = self.array[:]
        shuffle(self.array)
    def test_selectionsort(self):
        self.assertEqual(test_selection_sort(self.array), self.control, "selection sort is broken")
    def test_doubleselectionsort(self):
        self.assertEqual(test_double_selection_sort(self.array), self.control, "double selection sort is broken")

if __name__ == '__main__':
    unittest.main()