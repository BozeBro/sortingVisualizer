def quick_sort(array, bot=None, top=None):
    """This will do the quickSort sort"""
    if bot is None and top is None:
        bot = 0
        top = len(array) - 1
    if bot < top:
        index_p = top
        pivot = array[index_p]
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
                    yield i, top
                    pi = i
                    break
                elif array[i] <= array[top]:
                    pi = top
                    break
            elif array[i] > pivot >= array[i2]:
                array[i2], array[i] = array[i], array[i2]
                yield i2, i

        yield from quick_sort(array, bot, pi - 1)
        yield from quick_sort(array, pi + 1, top)