from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import shuffle


def mergesort(array, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort2(array, start, mid)
    yield from mergesort2(array, mid + 1, end)
    yield from merge2(array, start, mid, end)
    if start == 0 and end == len(array) - 1:
        yield 0, 0, 1


def merge(array, start, mid, end):
    merged, left, right = [], start, mid + 1

    while left <= mid and right <= end:
        if array[left] < array[right]:
            merged.append(array[left])
            yield left, array[left], 0
            left += 1
        else:
            merged.append(array[right])
            yield right, array[right], 2
            right += 1

    while left <= mid:
        merged.append(array[left])
        yield left, array[left], 0
        left += 1

    while right <= end:
        merged.append(array[right])
        yield right, array[right], 2
        right += 1

    for i, sorted_val in enumerate(merged):
        array[start + i] = sorted_val
        yield start + i, sorted_val, 0


def update(container):
    i, j, c = container
    if c == 2:
        if storage['store2'] != None:
            wedges[storage['store2']].set_color(storage['store3'])
        wedges[i].set_color('black')
        storage['store2'], storage['store3'] = i, storage[j]
        return
    if storage['store0'] != None:
        wedges[storage['store0']].set_color(storage['store1'])
    if c == 0:
        wedges[i].set_color('black')
    elif c == 1:
        return
    storage['store0'], storage['store1'] = i, storage[j]


number = 100
# length of the array
to_sort = [1 for m in range(number)]

plt.style.use('dark_background')
fig, ax = plt.subplots()
theme = plt.get_cmap('hsv')

length = [l for l in range(1, number + 1)]
shuffle(length)
# The actual array that will be sorted
test = [theme(i / (number - 1)) for i in length]
wedges, texts = ax.pie(to_sort, radius=4, startangle=90., shadow=True,
                       wedgeprops={'linewidth': False,
                                   'linestyle': 'solid'},
                       colors=test)
storage = {n: c for n, c in zip(length, test)}
storage['store0'], storage['store1'], \
storage['store2'], storage['store3'] = None, None, \
                                       None, None

# Storage to remember to switch off black marker
ax.axis('equal')
ani = FuncAnimation(fig, update, frames=mergesort(length, 0, len(length) - 1), repeat=False, interval=1,
                    blit=False)

plt.show()
