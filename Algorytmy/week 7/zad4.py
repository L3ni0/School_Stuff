from temp import Flota
import random
random.seed(1001)


n = 10
f = Flota()
f.generuj_flote(n, 10)

r_table = []
r_copy = []
print('tablica wejsciowa')
for i in range(n):
    r_table.append(f.share(i))
    r_copy.append(f.share(i))

r_copy[1] = ['ZBYYGCRMZF', 'AVF', 1528, 385, 19]
r_table[1] = ['ZBYYGCRMZF', 'AVF', 1528, 385, 19]

for i in r_table:
    print(i)


# podpunkt 1


def comand(l, r, table, param=None, ascending=1):   # partition
    pivot, ptr = table[r][param], l        # choosing pivot and pointer (last & first)
    for i in range(l, r):
        if ascending == 1:
            if table[i][param] <= pivot:
                table[i], table[ptr] = table[ptr], table[i]     # smaller than pivot to front
                ptr += 1
        else:
            if table[i][param] >= pivot:
                table[i], table[ptr] = table[ptr], table[i]     # smaller than pivot to front
                ptr += 1
    table[ptr], table[r] = table[r], table[ptr]     # swap
    return ptr


def conq(l, r, table, param=None, ascending=1):     # quicksort
    if len(table) == 1:         # end condition
        return table
    if l < r:
        pi = comand(l, r, table, param, ascending)
        conq(l, pi - 1, table, param, ascending)       # req for left
        conq(pi + 1, r, table, param, ascending)       # req for right
    return table


# 0 - id
# 1 - typ
# 2 - masa
# 3 - zasieg
# 4 - rozdielczosc


ans = int(input('Rosnaco - 1\tMalejoco - 0: '))
conq(0, len(r_table) - 1, r_table, int(input('\nPodaj parametr: ')), ans)
print('\ntablica koncowa\n')
for i in r_table:
    print(i)


# podpunkt 2


print('\npodpunkt 2\n')
print('\nTablica wejsciowa\n')
for i in r_copy:
    print(i)
ans2 = int(input('Rosnaco - 1\tMalejoco - 0: '))


def conq_adv(l, r, table, param=None, ascending=1):
    print(len(table))
    conq(l, r, table, param[0], ascending)
    # print(param)
    for p in range(len(param[1:])):
        start = l
        for i in range(len(table) - 1):
            if table[i][param[0]] != table[i + 1][param[0]]:
                print(p)
                table[start:i + 1] = conq(start, i, table[start:i + 1], param[1], ascending)
                start = i + 1
        table[start - 1:start] = conq(start - 1, start, table[start - 1:start], param[1], ascending)


def conq_adv2(l, r, table, param=None, ascending=1):
    # print(len(table))
    conq(l, r, table, param[0], ascending)
    # print(param)
    for p in range(len(param[1:])):
        start = l
        for i in range(len(table) - 1):
            if table[i][param[0]] != table[i + 1][param[0]]:
                # print(p)
                table[start:i + 1] = conq(start, i, table[start:i + 1], param[1], ascending)
                start = i + 1
        temp = 0
        for i in range(len(table) - 1, int(len(table)/2), -1):
            # print(i)
            if table[i][param[0]] == table[i - 1][param[0]]:
                temp += 1
            else:
                break
        print(temp)
        # print(start, len(table))
        # table[temp:] = conq(temp, len(table) - 1, table[temp:], param[1], ascending)


def conqujer_ez(l, r, table, param=None, ascending=1):
    for p in param:
        conq(l, r, table, p, ascending)


params = []
n = input('ile parametrow podasz?: ')
for i in range(1, int(n) + 1):
    params.append(int(input(f'Podaj parametr nr {i}: ')))


# conq_adv2(0, len(r_copy) - 1, r_copy, params, ans2)
conqujer_ez(0, len(r_copy) - 1, r_copy, reversed(params), ans2)
print('\ntablica koncowa\n')
for i in r_copy:
    print(i)

