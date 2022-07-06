import time
import matplotlib.pyplot as plt

with open('a.txt','r') as file:  # wcześnieszy generator pisałem w excelu i a łatwiej jest zaimportować z tekstu
    a = file.readlines()
    a = list(map(lambda x: float(x.replace(',','.')), a))


def generaotr_równomierny(a,n):
    h0 = time.time()
    X = [h0]
    for i in range(n):
        new_x = (X[i] * a[i%len(a)] + sum(X)) % 1
        X.append(new_x)
    del X[0]
    return X


def generator_rozklad_nomrlany(liczby_rownomierne): # zad 1
    if len(liczby_rownomierne)% 12 != 0:
        return 'musi być wielokrotność 12'

    X = []
    for i in range(len(liczby_rownomierne)//12):
        new_x = 0
        for j in range(12):
            new_x += liczby_rownomierne[12*i + j]

        X.append(new_x-6)
    return X


#zad 2
ciag_20 = generator_rozklad_nomrlany(generaotr_równomierny(a,240))
ciag_100 = generator_rozklad_nomrlany(generaotr_równomierny(a,1200))

with open('lista 4 ciag 20.txt','w') as file:
    for i in ciag_20:
        file.write(f"{i}\n")

with open('lista 4 ciag 100.txt','w') as file:
    for i in ciag_100:
        file.write(f"{i}\n")

def srednia(X):
    return sum(X)/len(X)

def mediana(X):
    X.sort()
    if len(X) % 2 == 0:
        return (X[len(X)//2] + X[len(X)//2 - 1]) / 2
    else:
        return X[len(X)//2 ]

def moda(X):
    najw = 0
    n_liczba = 0
    for wart in X:
        if X.count(wart) > najw:
            najw = X.count(wart)
            n_liczba = wart
    if najw == 1: # oznacza to że każda wartość wystepuje raz
        return 'brak mody'
    else:
        return n_liczba

def wariancja(X):
    sr = srednia(X)
    X = list(map(lambda x: (x - sr) ** 2, X))
    return sum(X)/len(X)

def odchylenie_std(X):
    return wariancja(X)**0.5

def skosnosc(X):
    sr = srednia(X)
    s = odchylenie_std(X)
    X = list(map(lambda x: (x - sr) ** 3, X))
    n = len(X)
    return n*sum(X)/((n-1)*(n-2)*s**3)

def kurtoza(X): #użyty wzór z excela aby się zgadzało z poprzednimi listami
    s = odchylenie_std(X)
    n = len(X)
    sr = srednia(X)
    suma = sum(list(map(lambda x: ((x-sr)/s)**4,X)))
    return (n*(n+1)*suma/((n-1)*(n-2)*(n-3)))-3*(n-1)**2/((n-2)*(n-3))

def kwantyl_gorny(X):
    X.sort()
    if len(X) % 2 == 0:
        return mediana(X[len(X)//2:])
    else:
        return mediana(X[len(X)//2+1:])

#zad 3
def statystyki(x1,x2):
    return f'''n\t20\t100
średnia: \t\t{srednia(x1)}\t{srednia(x2)}
mediana: \t\t{mediana(x1)}\t{mediana(x2)}
moda:    \t\t{moda(x1)}\t{moda(x2)}
ochylenie std: {odchylenie_std(x1)}\t{odchylenie_std(x2)}
wariancja: {wariancja(x1)}\t{wariancja(x2)}
skośnosc: \t\t{skosnosc(x1)}\t{skosnosc(x2)}
kurtoza: \t\t{kurtoza(x1)}\t{kurtoza(x2)}
kwantyl górny: {kwantyl_gorny(x1)}\t{kwantyl_gorny(x2)}
    '''

print(statystyki(ciag_20, ciag_100))

plt.hist(ciag_20)
plt.show()
plt.hist(ciag_100)
plt.show()


def test_t_student(x1, m):
    if len(x1) < 30:
        return ((srednia(x1)-m)/odchylenie_std(x1)) * (len(x1)-1)**0.5
    else:
        return ((srednia(x1)-m)/odchylenie_std(x1)) * len(x1)**0.5

def czy_sa_rowne(x1, x2):
    return (srednia(x1)-srednia(x2))/(odchylenie_std(x1)**2/len(x1) + odchylenie_std(x2)/len(x2))**0.5

print(f'test t studenta dla ciagu 20 elementowego: {test_t_student(ciag_20, 0)}')
print(f'test t studenta dla ciagu 100 elementowego: {test_t_student(ciag_100, 0)}')



with open('lista1 ciag 20.txt','r') as file:
    l1_20 = file.readlines()
    l1_20 = list(map(lambda x: float(x.replace(',','.')), l1_20))

with open('lista 1 ciag 100.txt','r') as file:
    l1_100 = file.readlines()
    l1_100 = list(map(lambda x: float(x.replace(',','.')), l1_100))

with open('lista 2 ciag 20.txt','r') as file:
    l2_20 = file.readlines()
    l2_20 = list(map(lambda x: float(x.replace(',','.')), l2_20))

with open('lista 2 ciag 100.txt','r') as file:
    l2_100 = file.readlines()
    l2_100 = list(map(lambda x: float(x.replace(',','.')), l2_100))

print(f'test t studenta dla listy 2 ciagu 20 elementowego: {test_t_student(l2_20, 0)}')
print(f'test t studenta dla list 2 ciagu 100 elementowego: {test_t_student(l2_100, 0)}')


print(f'czy średnia z listy 1 jest równa {czy_sa_rowne(ciag_20, l1_20)} dla ciagu 20el')
print(f'czy średnia z listy 1 jest równa {czy_sa_rowne(ciag_100, l1_100)} dla ciagu 100el')

print(f'czy średnia z listy 2 jest równa {czy_sa_rowne(ciag_20, l2_20)} dla ciagu 20el')
print(f'czy średnia z listy 2 jest równa {czy_sa_rowne(ciag_100, l2_100)} dla ciagu 100el')
