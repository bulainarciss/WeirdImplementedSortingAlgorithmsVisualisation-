import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
nr = 100
list_to_be_sorted = [0] * nr
index = [0] * nr
for w in range(nr):
    list_to_be_sorted[w] = random.randint(0, 2000)
    index[w] = w

ims = []

green_bars = []


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            mybar = plt.bar(index, arr, color='b')
            mybar[i].set_color('r')
            mybar[j].set_color('r')


            ims.append(mybar)


    arr[i + 1], arr[high] = arr[high], arr[i + 1]



    return (i + 1)


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr

    if low < high:

        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)



quickSort(list_to_be_sorted, 0, nr-1)
print("Hello!")
anim = animation.ArtistAnimation(fig, ims, interval=100, repeat_delay=0,
                                   blit=False, repeat=True)


plt.show()