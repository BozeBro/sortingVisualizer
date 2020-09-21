from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import shuffle

def insertionSort(array):
    for i in range(1, len(array)):
        temp, index = array[i], i - 1

        while index >= 0 and array[index] > temp:
            array[index + 1] = array[index]
            yield index + 1, array[index], 0
            index -= 1
        array[index + 1] = temp
        yield index + 1, temp, 1

def update(array):
    """The function that does the animating"""
    i, j, c = array
    if storage['store0'] != None:
        wedges[storage['store0']].set_color(storage['store1'])
    storage['store0'], storage['store1'] = i, storage[j]
    if c == 0:
        wedges[i].set_color('black')
    elif c == 1:
        wedges[i].set_color(storage[j])
    return wedges
if __name__ == "__main__":
    number = 50
    # length of the array
    to_sort = [1 for m in range(number)]

    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    theme = plt.get_cmap('hsv')

    length = [l for l in range(1, number+1)]
    shuffle(length)
    # The actual array that will be sorted
    test = [theme(i / (number - 1)) for i in length]
    wedges, texts = ax.pie(to_sort, radius=4, startangle=90., shadow=True,
                        wedgeprops={'linewidth': False,
                                    'linestyle': 'solid'},
                        colors=test)
    storage = {n: c for n, c in zip(length, test)}
    storage['store0'], storage['store1'] = None, None
    ax.axis('equal')
    # Storage to remember to switch off black marker
    ani = FuncAnimation(fig, update, frames=insertionSort(length), repeat=False, interval=10,
                        blit=True)

    plt.show()