from matplotlib import pyplot as plt
from matplotlib import animation
from random import shuffle
import argparse
from algorithmsv2 import *

parser = argparse.ArgumentParser(description="Sorting Algorithm Visualization")
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

#functinos dictionary can be found in algorithmsv2 __init__.py file
function = functions[args.function]


def sortalgo(f, function=function):
    def wrapper(*args):
        if function.__name__ == "merge_sort":
            return merge_update(*args)
        return f(*args)

    return wrapper


def merge_update(swapped):
    i, j = swapped
    bar_rects[i].set_height(j)


@sortalgo
def update(swapped):
    i, j = 0, 1
    while j < len(swapped):
        x, y = swapped[i], swapped[j]
        tmpx, tmpy = bar_rects[x].get_height(), bar_rects[y].get_height()
        bar_rects[x].set_height(tmpy)
        bar_rects[y].set_height(tmpx)
        i += 1
        j += 1


if __name__ == "__main__":
    number = args.number

    unsorted = [x for x in range(1, number + 1)]
    shuffle(unsorted)

    plt.style.use("dark_background")
    fig, ax = plt.subplots()
    plt.title(function.__name__)

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    plt.tick_params(
        axis="both",  # If changes only apply to x, y or both
        which="both",  # If major, minor, or both are affected
        bottom=False,  # x axis ticks
        left=False,  # y axis ticks
        labelleft=False,  # y axis label
        labelbottom=False,  # x axis label
    )

    bar_rects = plt.bar(
        range(len(unsorted)), unsorted, width=1, align="edge", color="white"
    )
    ani = animation.FuncAnimation(
        fig, update, interval=args.interval, frames=function(unsorted), blit=False, repeat=False
    )
plt.show()
