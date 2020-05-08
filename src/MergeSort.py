from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from random import shuffle


def mergesort2(A, start, end):
    # This function does not use splices but maintains original list

    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort2(A, start, mid)
    yield from mergesort2(A, mid + 1, end)
    yield from merge2(A, start, mid, end)
    if start == 0 and end == len(A) - 1:
        yield 0, 0, 1


def merge2(A, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield start + i, sorted_val, 0


def update(array):
    i, j, c = array
    if store[0] != None:
        wedges[store[0]].set_color(store[1])
    if c == 0:
        wedges[i].set_color('black')
    elif c == 1:
        return
    store[0], store[1] = i, storage[j]


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
store = [None, None]
storage = {n: c for n, c in zip(length, test)}
# Storage to remember to switch off black marker
ax.axis('equal')
ani = FuncAnimation(fig, update, frames=mergesort2(length, 0, len(length) - 1), repeat=False, interval=1,
                    blit=False)

plt.show()
