def heap_sort(array):
    n = len(array)
    for i in reversed(range(n//2)):
        yield from max_heapify(array, i, n)
    for i in reversed(range(n)):
        array[0], array[i] = array[i], array[0]
        yield 0, i
        yield from max_heapify(array, 0, i)

def max_heapify(array, index, length):
    left = index * 2 + 1
    right = index * 2 + 2
    large = index
    if left < length and array[left] > array[large]:
        large = left
    if right < length and array[right] > array[large]:
        large = right
    if large != index:
        array[index], array[large] = array[large], array[index]
        yield index, large
        yield from max_heapify(array, large, length)

def test_heap_sort(array):
    n = len(array)
    for i in reversed(range(n//2)):
        test_max_heapify(array, i, n)
    for i in reversed(range(n)):
        array[0], array[i] = array[i], array[0]
        test_max_heapify(array, 0, i)

def test_max_heapify(array, index, length):
    left = index * 2 + 1
    right = index * 2 + 2
    large = index
    if left < length and array[left] > array[large]:
        large = left
    if right < length and array[right] > array[large]:
        large = right
    if large != index:
        array[index], array[large] = array[large], array[index]
        test_max_heapify(array, large, length)

if __name__ == "__main__":
    from random import shuffle
    array = [i+1 for i in range(1000)]
    shuffle(array)
    test_heap_sort(array)
    print(array == [i+1 for i in range(1000)])
