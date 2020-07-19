def bubbleSort(array):
    """Sorting Algorithm compares every pair of items and will switch if the right item is smaller than the left."""
    is_sorted = True
    while is_sorted:
        count = 1
        is_sorted = False
        for i in range(len(array) - count):
            if array[i] > array[i + 1]:
                is_sorted = True
                array[i], array[i + 1] = array[i + 1], array[i]
                yield i + 1, i, 0
        count += 1
    yield i + 1, i, 1
    # for m in range(len(array) - 1):
    # yield m, m + 1, array, True
    # yield 'Done', 'Done', 0, 'Done'


