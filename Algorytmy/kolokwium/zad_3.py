from zad_2 import *
import matplotlib.pyplot as plt
from matplotlib import style
import time


def mierz_czas_i_wykres(do_ilu):
    czasy = []
    for i in range(2,do_ilu+1):
        lista = tworzenie_listy(i)

        start = time.time()
        wynik = sortowanie_listy(lista)
        czasy.append(time.time()-start)

    plt.style.use('bmh')
    plt.plot(range(2,do_ilu+1), czasy)
    plt.title('czas wykonania algorytmu w zaleznosci od liczby wierszy')
    plt.xlabel('liczba wierszy')
    plt.ylabel('czas w sekundach')
    plt.show()
    return czasy

mierz_czas_i_wykres(300)