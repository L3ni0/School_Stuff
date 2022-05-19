import time
import matplotlib.pyplot as plt
import math

with open('a.txt','r') as file:  # wcześnieszy generator pisałem w excelu i a łatwiej jest zaimportować z tekstu
    a = file.readlines()
    a = list(map(lambda x: float(x.replace(',','.')), a))


def generaotr_równomierny(a,n):
    h0 = time.time()
    X = [h0]
    for i in range(n):
        new_x = (X[i] * a[i%len(a)] + sum(X) + 35) % 1
        X.append(new_x)
    del X[0]
    return X

def funkcja(x):
    return math.exp(-(x**2)/2)

liczby1 = generaotr_równomierny(a,100002)

wynik = sum(map(funkcja, liczby1))/len(liczby1)
print(wynik)

def problem_plecakowy(X):
    max_cap = 15 # maksymalna pojemnosc plecaka
    weights = [2, 4, 6] # ilosc miejsca jakie zuzywaja pudelka
    walue = [2,3,10] # wartosc pudelka gdzie weights[i] odpowiada walue[i] choc w przypadku liczenia nie jest potrzebne
    combinations = [] # dopuszczalne kombicane

    X = list(map(lambda x: (x*10)//1, X)) #<- potrzebujemy całkowitych liczb, w tym problemie wystarczą liczby [0,10]

    for i in range(0,len(X)-2,3):
        if X[i]*weights[0] + X[i+1]*weights[1] + X[i+2]*weights[2] <= max_cap: # sprawdzamy czy sie zmiescimy do plecaka
            if not [X[i], X[i+1], X[i+2]] in combinations: # sprawdzamy czy kombinacja juz nie wystepowala
                combinations.append([X[i], X[i+1], X[i+2]]) # dodajemy kombinacje
    print(combinations)
    return len(combinations) # zwracamy ilosc kombinacji



print(problem_plecakowy(liczby1))

def przedsiebiorstwo(cena,zarowka_koszt,produkcja):
    zarowka_koszt = round((zarowka_koszt+ 2), 2) # jako ze mój generator losuje wartoscci z przedzialu [0,1]
    # zwieksze tą wartość aby była miedzy [2,3] i było ją można wyrazić w złotówkach
    cena = round((cena * 5 + 5), 2) # aby wyniki były w przedziale [5zł, 10zł]
    produkcja = ((produkcja+1) * 1000) // 1 # dzięki temu wyniki znajdują się w przedziale [1000, 2000]
    koszt_staly = 50000

    return ((cena-zarowka_koszt)*produkcja*12) - koszt_staly


szacowana_wartosc = 0
for i in range(0,len(liczby1)-2,3):
    szacowana_wartosc += przedsiebiorstwo(liczby1[i], liczby1[i+1], liczby1[i+2])
szacowana_wartosc = round(szacowana_wartosc / (len(liczby1) // 3),2)
print(szacowana_wartosc)