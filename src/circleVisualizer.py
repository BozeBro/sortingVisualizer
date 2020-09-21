from random import shuffle
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from algorithmsv1.InsertionCircle import insertionSort

def update(to_swap):
    """The function that does the animating"""
    if store[0] is not None:
        # Change wedge to its actual color (not black)
        wedges[store[0]].set_color(store[1])

    i, j, c = to_swap
    # Option to have the circle turn green when completed. Only available in bubble sort atm.
    # Uncomment the yield in AlgosForCircle in the bubbleSort Function
    i_color = wedges[i].get_facecolor()
    wedges[i].set_color(wedges[j].get_facecolor())

    if c == 0:
        # Black Marker
        wedges[j].set_color('black')
    elif c == 1:
        # Used at the end of an algorithm. 
        # Change black marker to tru color
        wedges[j].set_color(i_color)
    store[0], store[1] = j, i_color

number = 40
wedge_length = [1 for i in range(number - 1)]
to_sort = [i for i in range(number - 1)]
shuffle(to_sort)
# number is the amount of wedges
# length makes wedges with equal length
# to_sort is the actual array that will be sorted
plt.style.use('dark_background')
theme = plt.get_cmap('Reds')

fig, ax = plt.subplots()
colors = [theme(i / (number - 1)) for i in to_sort]
wedges, texts = ax.pie(wedge_length, radius=4, startangle=90.,
                       wedgeprops={'linewidth': False,
                                   'linestyle': 'solid'},
                       colors=colors)
ax.axis('equal')
#For black line
store = [None, None]

# Storage to remember to switch off black marker
ani = FuncAnimation(fig, update, frames=insertionSort(to_sort), repeat=False, interval=1,
                    blit=False)
plt.show()
