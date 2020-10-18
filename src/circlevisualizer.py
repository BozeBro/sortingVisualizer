from random import shuffle
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from algorithmsv2 import *

parser = argparse.ArgumentParser(description="Sorting Algorithm Visualizer")
parser.add_argument(
    "-f",
    "--function",
    type=str,
    default="quick_sort",
    metavar="",
    help="Sorting function to visualize. Current options are Quicksort, Mergesort, Selectionsort, Bubblesort, Insertionsort, Heapsort, Doubleselectionsort",
)
parser.add_argument(
    "-n", "--number", type=int, default=50, metavar="", help="How many elements to sort"
)
parser.add_argument(
    "-i",
    "--interval",
    type=int,
    default=1,
    metavar="",
    help="How fast the visualization is. 1000 is 1000 milliseconds or 1 second",
)
args = parser.parse_args()

function = args.function

def sortalgo(f, function=function):
    def wrapper(*args):
        if function.__name__ == 'merge_sort':
            return merge_update(*args)
        return f(*args)
    return wrapper

def merge_update(swapped):
    i, j = swapped
    wedges[i].set_color(theme(j/len(unsorted)))

@sortalgo
def update(swapped):
    i, j = 0, 1
    while j < len(swapped):
        x, y = swapped[i], swapped[j]
        tmpx, tmpy = wedges[x].get_facecolor(), wedges[y].get_facecolor()
        wedges[x].set_color(tmpy)
        wedges[y].set_color(tmpx)
        i += 1
        j += 1

number = args.n
wedge_length = [1 for _ in range(number)]
unsorted = [i+1 for i in range(number)]
shuffle(unsorted)

plt.style.use('dark_background')
theme = plt.get_cmap('hsv')
fig, ax = plt.subplots()
colors = [theme(i / (number)) for i in unsorted]
wedges, texts = ax.pie(wedge_length, radius=4, startangle=90.,
                       wedgeprops={'linewidth': False,
                                   'linestyle': 'solid'},
                       colors=colors)
ax.axis('equal')

ani = FuncAnimation(fig, update, frames=function(unsorted), repeat=False, interval=args.interval,
                    blit=False)
plt.show()