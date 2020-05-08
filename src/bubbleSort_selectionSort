from random import randint
from random import shuffle


def bubbleSort(array):
    """Sorting Algorithm compares every pair of items and will switch if the right item is smaller than the left."""
    sorted = True
    while sorted:
        count = 1
        sorted = False
        for i in range(len(array) - count):
            if array[i] > array[i + 1]:
                sorted = True
                array[i], array[i + 1] = array[i + 1], array[i]
                yield i + 1, i, 0
        count += 1
    yield i + 1, i, 1
    # for m in range(len(array) - 1):
    # yield m, m + 1, array, True
    # yield 'Done', 'Done', 0, 'Done'

def selectionSort(array):
    """selection sort algorithm"""
    i = 0
    while i != len(array):
        # is the starting point
        small = i
        # The smallest number is automatically the first one
        for check in range(i + 1, len(array)):
            # Check if check is smaller than small
            if array[small] > array[check]:
                small = check
        # At the end of the loop, we will have the smallest and we need to switch
        array[i], array[small] = array[small], array[i]

        yield i, small, 0
        i += 1
        # upgrade i so the starting point is moved
    yield 0, 0, 1

