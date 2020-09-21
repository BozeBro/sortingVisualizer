def selectionSort(array):
    """selection sort algorithm"""
    i = 0
    while i != len(array):
        # is the starting point
        small = i
        # The smallest number is automatically the first one
        for check in range(i + 1, len(array)):
            # Check if check is smaller than small
            yield check, check, 0
            if array[small] > array[check]:
                small = check
            #yield check, small, 0
        # At the end of the loop, we will have the smallest and we need to switch
        array[i], array[small] = array[small], array[i]

        yield i, small, 0
        i += 1
        # upgrade i so the starting point is moved
    yield 0, 0, 1

