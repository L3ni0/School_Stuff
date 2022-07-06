import random


def tworzenie_listy(n_wierszy:int):
    lista = []
    for _ in range(n_wierszy):
        lista.append([random.randint(0,99),random.randint(0,99)])
    return lista



def sortowanie_listy(lista:list):

    for _ in range(len(lista)*2):
        for i in range(len(lista)-1):
            if lista[i][0] > lista[i+1][0] and lista[i][1] % 2 == 1:
                lista[i], lista[i+1] = lista[i+1], lista[i]
            elif lista[i][0] < lista[i+1][0] and lista[i][1] % 2 == 0:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

    return lista

if __name__ == '__main__':
    n_wierszy = int(input('prosze podać liczbe wierszy: '))
    l = tworzenie_listy(n_wierszy)
    print(l)
    print(sortowanie_listy(l))
