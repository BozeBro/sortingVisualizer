def double_selection_sort(array): 
    bot = 0
    top = len(array) - 1
    while(bot < top): 
        small = big = array[bot] 
        small_ind = big_ind = bot
        for i in range(bot, top + 1):
            val = array[i]
            if val > big: 
                big = val
                big_ind = i
            elif val < small: 
                small = val
                small_ind = i
            yield i, i
        array[bot], array[small_ind] = array[small_ind], array[bot]
        yield bot, small_ind
        if (array[small_ind] == big): 
            array[top], array[small_ind] = array[small_ind], array[top]
            yield top, small_ind
        else: 
            array[top], array[big_ind] = array[big_ind], array[top]
            yield top, big_ind
        bot += 1
        top -= 1
    return array

def test_double_selection_sort(array): 
    bot = 0
    top = len(array) - 1
    while(bot < top): 
        small = big = array[bot] 
        small_ind = big_ind = bot
        for i in range(bot, top + 1):
            val = array[i]
            if val > big: 
                big = val
                big_ind = i
            elif val < small: 
                small = val
                small_ind = i
        array[bot], array[small_ind] = array[small_ind], array[bot]
        if (array[small_ind] == big): 
            array[top], array[small_ind] = array[small_ind], array[top]
        else: 
            array[top], array[big_ind] = array[big_ind], array[top]
        bot += 1
        top -= 1
    return array

            

