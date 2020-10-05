from random import shuffle
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from algorithmsv2 import *

function = selection_sort

def sortalgo(f, function=function):
    def wrapper(*args):
        if function.__name__ == 'merge_sort':
            return merge_update(*args)
        return f(*args)
    return wrapper

def merge_update(swapped):
    i, val = swapped
    wedges[i].set_color(theme(val))

@sortalgo
def update(swapped):
    i, j = swapped
    tmpi, tmpj = wedges[i].get_facecolor(), wedges[j].get_facecolor()
    wedges[i].set_color(tmpj)
    wedges[j].set_color(tmpi)

number = 500
wedge_length = [1 for _ in range(number)]
to_sort = [i+1 for i in range(number)]
shuffle(to_sort)

plt.style.use('dark_background')
theme = plt.get_cmap('hsv')
fig, ax = plt.subplots()
colors = [theme(i / (number)) for i in to_sort]
wedges, texts = ax.pie(wedge_length, radius=4, startangle=90.,
                       wedgeprops={'linewidth': False,
                                   'linestyle': 'solid'},
                       colors=colors)
ax.axis('equal')

ani = FuncAnimation(fig, update, frames=function(to_sort), repeat=False, interval=1,
                    blit=False)
plt.show()