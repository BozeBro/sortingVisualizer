def insertion_sort(array):
    for i in range(1, len(array)):
        cur_val, index = array[i], i - 1
        while index > -1 and array[index] > cur_val:
            array[index + 1], array[index] = array[index], array[index + 1]
            yield index + 1, index
            index -= 1
        array[index + 1] = cur_val
        yield index, index
