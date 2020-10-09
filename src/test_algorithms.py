import unittest
from random import shuffle
from algorithmsv2 import *

class TestAlgorithms(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.array = [i for i in range(100)]
        self.control = self.array[:]
        shuffle(self.array)
    def test_selectionsort(self):
        self.assertEqual(test_selection_sort(self.array), self.control, "selection sort is broken")
    def test_doubleselectionsort(self):
        self.assertEqual(test_double_selection_sort(self.array), self.control, "double selection sort is broken")
    def test_quicksort(self):
        self.assertEqual(test_quick_sort(self.array), self.control, "quick sort is broken")
    def test_bubblesort(self):
        self.assertEqual(test_bubble_sort(self.array), self.control, "bubble sort is broken")
    def test_mergesort(self):
        self.assertEqual(test_merge_sort(self.array), self.control, "merge sort is broken")
    def test_insertionsrt(self):
        self.assertEqual(test_insertion_sort(self.array), self.control, "insertion sort is broken")
    def test_heap_sort(self):
        self.assertEqual(test_heap_sort(self.array), self.control, "heap sort is broken")
    

if __name__ == '__main__':
    unittest.main()