import numpy as np

np.random.seed(1000)

x = 10
y = 10
maximum = 4

t = np.random.randint(1, maximum, size=(x, y))
print('Tablica wejsciowa:\n')
for row in t:
    print(row)
# print(list(t[0]), type(list(t[0])))


def poz_sort(table):
    y = len(table[0])
    for index in range(y - 1, -1, -1):
        table.sort(key=lambda pair: pair[index])
    return table


poz_sort(list(t))
print('\nPosortowana tablica\n')
for i in poz_sort(list(t)):
    print(i)
