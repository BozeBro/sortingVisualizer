from random import randint


def quickSort(array, bot, top):
    if bot < top:
        index_p = randint(bot, top)
        pivot = array[index_p]
        array[index_p], array[top] = array[top], array[index_p]
        yield array
        i = bot
        i2 = top - 1
        while True:
            while array[i] <= pivot and i < i2:
                # This should get the number greater than pivot
                i += 1
            while array[i2] > pivot and i2 > i and i2 > bot:
                # This should get the number less than the pivot
                i2 -= 1
            if i >= i2:
                if array[i] > array[top]:
                    array[i], array[top] = array[top], array[i]
                    yield array
                    pi = i
                    break
                elif array[i] <= array[top]:
                    pi = top
                    break
            elif array[i] > pivot >= array[i2]:
                array[i2], array[i] = array[i], array[i2]
                yield array
        yield from quickSort(array, bot, pi - 1)
        yield from quickSort(array, pi + 1, top)


def bubbleSort(array):
    count = 1
    while count != (length:=len(array)):
        for i in range(length - count):
            if array[i] > array[i + 1]:
                yield i, i + 1, 0
                array[i], array[i + 1] = array[i + 1], array[i]
                #yield array, i, i + 1
        count += 1
    yield i, i + 1, 1


def merge(lside, rside, array, bot, original):
    combined = []
    while lside and rside:
        if lside[0] <= rside[0]:
            combined.append(lside.pop(0))
        elif lside[0] > rside[0]:
            combined.append(rside.pop(0))
    if lside:
        combined += lside
    elif rside:
        combined += rside
    for i, sorted_val in enumerate(combined):
        array[bot + i] = sorted_val
        original[bot + i] = sorted_val
        yield original


def mergeSort(array, original, bot=0):

    top = len(array) - 1
    if bot < top:
        mid = (top + 1 - bot) // 2
        lside = array[bot:mid]  # Left array
        rside = array[mid:top + 1]  # right array
        yield from mergeSort(lside, original)
        yield from mergeSort(rside, original)
        yield from merge(lside, rside, array, bot, original)
        yield original


'''Mergesort2 and merge2 are borrowed functions from https://github.com/nrsyed/sorts/blob/master/python/sorts.py#L67'''


def mergesort2(array, start, end):
    # This function does not use splices but maintains original list

    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort2(array, start, mid)
    yield from mergesort2(array, mid + 1, end)
    yield from merge2(array, start, mid, end)
    yield array


def merge2(array, start, mid, end):
    merged = []
    left = start
    right = mid + 1

    while left <= mid and right <= end:
        if array[left] < array[right]:
            merged.append(array[left])
            left += 1
        else:
            merged.append(array[right])
            right += 1

    while left <= mid:
        merged.append(array[left])
        left += 1

    while right <= end:
        merged.append(array[right])
        right += 1

    for i, sorted_val in enumerate(merged):
        array[start + i] = sorted_val
        yield array


def selectionSort(array):
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

        yield array
        i += 1
        # upgrade i so the starting point is moved


def insertionSort(array):
    for i in range(1, len(array)):
        point1 = array[i]
        j = i - 1
        while j >= 0 and point1 < array[j]:
            # Individually moving each piece
            array[j + 1] = array[j]
            yield array
            j -= 1
        array[j + 1] = point1
        yield array
