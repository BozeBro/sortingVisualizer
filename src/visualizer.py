from matplotlib import pyplot as plt
from matplotlib import animation
from algoBars import *
from random import shuffle

iteration = [0]


# return bar_rects
def animate(array, bar_rects, iteration):
    '''i, j, c = array
    iteration[0] += 1
    text.set_text(f'# of function calls: {iteration[0]}')
    h1 = bar_rects[j].get_height()
    bar_rects[j].set_height(bar_rects[i].get_height())
    bar_rects[i].set_height(h1)'''
    iteration[0] += 1
    text.set_text(f'# of function calls: {iteration[0]}')
    for i, v in enumerate(bar_rects):
        if i == len(array):
            return
        v.set_height(array[i])
    # return


if __name__ == '__main__':
    number = int(input("How big is the array to be sorted? "))
    options = "What method would you like to use? " \
              "\n quicksort (q)" \
              "\n bubblesort (b)" \
              "\n mergesort (m1)" \
              "\n mergesort (alternative) (m2)" \
              "\n selectionsort (s)" \
              "\n insertsort (i)"
    sort = input(options)
    unsorted = [x for x in range(1, number + 1)]
    shuffle(unsorted)

    if sort == 'q':
        title = 'Quicksort'
        algos = quickSort(unsorted, 0, len(unsorted) - 1)
    elif sort == 'b':
        title = 'Bubblesort'
        algos = bubbleSort(unsorted)
    elif sort == 'm1':
        title = 'Mergesort 1'
        algos = mergeSort(unsorted, unsorted)
    elif sort == 'm2':
        title = 'Mergesort 2'
        algos = mergesort2(unsorted, 0, len(unsorted) - 1)
    elif sort == 's':
        title = 'Selectionsort'
        algos = selectionSort(unsorted)
    elif sort == 'i':
        title = 'Insertionsort'
        algos = selectionSort(unsorted)
    else:
        raise NameError
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    plt.title(title)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.tick_params(
        axis='both',  # If changes only apply to x, y or both
        which='both',  # If major, minor, or both are affected
        bottom=False,  # x axis ticks
        left=False,  # y axis ticks
        labelleft=False,  # y axis label
        labelbottom=False  # x axis label
    )

    text = ax.text(0.009, 0.95, "", transform=ax.transAxes)
    interval = [0]
    text.set_text(f'# numbers of operations: {iteration[0]}')
    bar_rects = plt.bar(range(len(unsorted)), unsorted,
                        width=1, align='edge', color='cyan', edgecolor='b')
    ani = animation.FuncAnimation(fig, animate, fargs=(bar_rects, iteration),
                                  interval=100, frames=algos, blit=False, repeat=False)
    # f = r'C:\Users\benoz\Desktop\Sorting_videos\quicksort_neg.gif'
    # writervideo = animation.PillowWriter(fps=120)
    # ani.save(f, writer=writervideo)
plt.show()
