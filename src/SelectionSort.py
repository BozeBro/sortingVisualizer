from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import shuffle
from random import randint


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
        # At the end of the loop, we will have the smallest and we need to switch
        array[i], array[small] = array[small], array[i]

        yield i, small, 0
        i += 1
        # upgrade i so the starting point is moved
    yield 0, 0, 1


def update(array):
    """The function that does the animating"""
    if store[0] != None:
        wedges[store[0]].set_color(store[1])

    i, j, c = array
    mvp = wedges[i].get_facecolor()
    wedges[i].set_color(wedges[j].get_facecolor())

    if c == 0:
        # So the black marker does not remain
        wedges[j].set_color('black')
    elif c == 1:
        wedges[j].set_color(mvp)
    store[0], store[1] = j, mvp

number = 50
# length of the array
to_sort = [1 for m in range(number)]

plt.style.use('dark_background')
fig, ax = plt.subplots()
theme = plt.get_cmap('twilight')

length = [l for l in range(1, number+1)]
shuffle(length)
# The actual array that will be sorted
test = [theme(i / (number - 1)) for i in length]
wedges, texts = ax.pie(to_sort, radius=4, startangle=90., shadow=True,
                       wedgeprops={'linewidth': False,
                                   'linestyle': 'solid'},
                       colors=test)
store = [None, None]
ax.axis('equal')
ani = FuncAnimation(fig, update, frames=selectionSort(length), repeat=False, interval=1,
                    blit=False)

plt.show()
