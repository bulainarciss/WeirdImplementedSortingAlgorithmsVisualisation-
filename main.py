import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
nr = 300
list_to_be_sorted = [0] * nr
index = [0] * nr
for w in range(nr):
    list_to_be_sorted[w] = random.randint(0, 2000)
    index[w] = w

mybar = plt.bar(index, list_to_be_sorted, color='red')


def bubble_sort(t):


    for i in range(t % nr, nr):
        for j in range(i+1, nr):
            if list_to_be_sorted[i] > list_to_be_sorted[j]:
                list_to_be_sorted[i], list_to_be_sorted[j] = list_to_be_sorted[j], list_to_be_sorted[i]
                mybar[i].set_height(list_to_be_sorted[i])
                mybar[j].set_height(list_to_be_sorted[j])
                mybar[i].set_color('g') # for slow must be commented

            if i == nr - 2: # for slow must be commented
                mybar[nr-1].set_color('g') # for slow must be commented

            #return mybar # the way it works, but slow
        return mybar










anim=animation.FuncAnimation(fig, bubble_sort,repeat=True,blit=True,frames=int(nr*(nr+1)/2)+1,
                             interval=1)
plt.show()