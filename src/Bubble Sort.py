from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from BubbleSortAlgorithm import bubbleSort
from random import shuffle


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
store = [None, None]
# Storage to remember to switch off black marker
ani = FuncAnimation(fig, update, frames=bubbleSort(length), repeat=False, interval=1,
                    blit=False)

plt.show()
