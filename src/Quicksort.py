from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import shuffle
from random import randint

def quickSort(array, bot, top):
    """This will do the quickSort sort"""
    if bot < top:
        index_p = randint(bot, top)
        pivot = array[index_p]
        array[index_p], array[top] = array[top], array[index_p]
        yield index_p, top, 0
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
                    yield i, top, 0
                    pi = i
                    break
                elif array[i] <= array[top]:
                    pi = top
                    break
            elif array[i] > pivot >= array[i2]:
                array[i2], array[i] = array[i], array[i2]
                yield i, i2, 0
        yield from quickSort(array, bot, pi - 1)
        yield from quickSort(array, pi + 1, top)
        if bot == 0 and top == len(array) - 1:
            yield 0, 0, 1

def update(array):
    """The function that does the animating"""
    if store[0] != None:
        wedges[store[0]].set_color(store[1])
        wedges[store[2]].set_color(store[3])
    i, j, c = array

    mvp = wedges[i].get_facecolor()
    other = wedges[j].get_facecolor()
    wedges[i].set_color(other)

    if c == 0:
        # So the black marker does not remain
        wedges[j].set_color('black')
        wedges[i].set_color('black')
    elif c == 1:
        wedges[j].set_color(mvp)
        wedges[i].set_color(other)
    store[0], store[1] = j, mvp
    store[2], store[3] = i, other
    # return wedges
    # return is for blitting purposes. However, the marker gets turned off.


number = 300
# length of the array
to_sort = [1 for m in range(number - 1)]
# to_sort makes wedges with equal length

plt.style.use('dark_background')
fig, ax = plt.subplots()
theme = plt.get_cmap('hsv')

length = [l for l in range(number - 1)]
shuffle(length)
# The actual array that will be sorted
test = [theme(i / (number - 1)) for i in length]
wedges, texts = ax.pie(to_sort, radius=4, startangle=90., shadow=True,
                       wedgeprops={'linewidth': False,
                                   'linestyle': 'solid'},
                       colors=test)

ax.axis('equal')
store = [None, None, None, None]
# Storage to remember to switch off black marker
ani = FuncAnimation(fig, update, frames=quickSort(length, 0, len(length) - 1), repeat=False, interval=1,
                    blit=False)

plt.show()
