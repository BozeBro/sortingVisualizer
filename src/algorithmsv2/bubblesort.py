def bubble_sort(array):
    """Sorting Algorithm compares every pair of items and will switch if the right item is smaller than the left."""
    count = 1
    while count != (length:=len(array)):
        for i in range(length - count):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                yield i + 1, i
        count += 1

def bubble_sort(array):
    """Sorting Algorithm compares every pair of items and will switch if the right item is smaller than the left."""
    count = 1
    while count != (length:=len(array)):
        for i in range(length - count):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        count += 1

