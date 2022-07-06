import random
import matplotlib.pyplot as plt
import numpy as np

kwik = []
cols_kwik = []
czip = []
cols_czip = []
cols = []


def heapify(table, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and table[i] < table[l]:
        largest = l

    if r < n and table[largest] < table[r]:
        largest = r

    if largest != i:
        table[i], table[largest] = table[largest], table[i]
        heapify(table, n, largest)


    cols[i] = 'red'
    cols[largest] = 'red'
    cols_czip.append(cols.copy())
    czip.append(table.copy())
    plt.bar(np.arange(len(table)), table, color=cols)
    plt.show()
    cols[i] = 'black'
    cols[largest] = 'black'


def heapSort(table):
    n = len(table)

    for i in range(n // 2, -1, -1):
        heapify(table, n, i)

    for i in range(n - 1, 0, -1):
        table[i], table[0] = table[0], table[i]

        heapify(table, i, 0)


table = []
table_copy = []
for i in range(50):
    a = random.randint(1, 50)
    table.append(a)
    table_copy.append(a)
    cols.append('black')

heapSort(table)
print(table_copy)


def comand(l, r, table, ascending=1):       # partition
    pivot, ptr = table[r], l        # choosing pivot and pointer (last & first)
    for i in range(l, r):
        if ascending == 1:
            if table[i] <= pivot:
                table[i], table[ptr] = table[ptr], table[i]
                ptr += 1
        else:
            if table[i] >= pivot:
                table[i], table[ptr] = table[ptr], table[i]
                ptr += 1

        cols[i] = 'red'
        cols[ptr] = 'red'
        cols_kwik.append(cols.copy)
        kwik.append(table.copy())
        plt.bar(np.arange(len(table)), table, color=cols)
        plt.show()
        cols[i] = 'black'
        cols[ptr] = 'black'

    table[ptr], table[r] = table[r], table[ptr]     # swap
    return ptr


def conq(l, r, table, ascending=1):     # quicksort
    if len(table) == 1:         # end condition
        return table
    if l < r:
        pi = comand(l, r, table, ascending)
        conq(l, pi - 1, table, ascending)       # req for left
        conq(pi + 1, r, table, ascending)       # req for right
    return table


conq(0, len(table_copy) - 1, table_copy, 1)
print(table)
print(table_copy)


