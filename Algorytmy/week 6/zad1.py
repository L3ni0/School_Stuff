import random


class Robot:

    def __init__(self, id, typ, masa, zasieg, rozdzielczosc):
        self.id = id
        self.typ = typ
        self.masa = masa
        self.zasieg = zasieg
        self.rozdzielczosc = rozdzielczosc

    def show(self):
        return [self.id, self.typ, self.masa, self.zasieg, self.rozdzielczosc]


class Flota:

    def __init__(self):
        self.wektor= []

    def dodaj_robota(self,id, typ, masa, zasieg, rozdzielczosc):
        self.wektor.append(Robot(id, typ, masa, zasieg, rozdzielczosc))

    def generuj_opis(self, N):
        id = ''.join([chr(random.randint(65,90)) for _ in range(N)])
        typ = random.choice(['AUV','AVF','AGV'])
        masa = random.randint(50,2000)
        zasieg = random.randint(1,1000)
        rozdzielczosc = random.randint(1,30)
        self.dodaj_robota(id, typ, masa, zasieg, rozdzielczosc)

    def generuj_flote(self, M, N):
        for _ in range(M):
            self.generuj_opis(N)

    def wyswietl(self):
        print('|'.join([str(j).ljust(14) for j in ['identyfikator','typ','masa','zasieg','rozdzielczosc']]))
        for info in self.wektor:
            info = info.show()
            print('|'.join([str(j).ljust(14) for j in info]))

    def zapisz_do_pliku(self,plik):
        with open(plik,'w') as plik:
            for info in self.wektor:
                info = info.show()
                plik.write(' '.join(str(j) for j in info)+'\n')

    def odczytaj_plik(self,plik):
        with open(plik, 'r') as plik:
            for linijka in plik.readlines():
                id,t,m,z,r = [int(i) if i.isdigit() else i for i in linijka.strip().split()]
                self.dodaj_robota(id,t,m,z,r)

    # zadanie 1
    def wyszukiwanie_lin(self, param, wart):
        if not param:
            return None
        print(self.wektor[0].show()[int(param)])  # wartosc robota 0 w parametrze param
        for i in range(len(self.wektor)):
            if self.wektor[i].show()[int(param)] == wart:
                return self.wektor[i].show()
        else:
            return None

    def wyszukiwanie_zaaw(self, iden=None, typ=None, mas=None, zas=None, rez=None):
        lista = [iden, typ, mas, zas, rez]
        temp = [[], [], [], [], []]
        print(lista)
        for item in lista:
            l = 0
            if item:
                for i in range(len(self.wektor)):
                    if self.wektor[i].show()[lista.index(item)] == item:
                        temp[lista.index(item)].append(self.wektor[i])
                        l += 1
                print(f'znaleziono {l} robotow bazujac na parametrze {item}')
        # print(temp[1][0].show())
        result = temp[0] + temp[1] + temp[2] + temp[3] + temp[4]
        final = list(set(result))
        if final:
            return final[0].show()
        else:
            return None

    def wyszukiwanie_final(self, iden=None, typ=None, mas=None, zas=None, rez=None):
        lista = [iden, typ, mas, zas, rez]
        temp = [[], [], [], [], []]
        print(lista)
        for item in lista:
            l = 0
            if item:
                for i in range(len(self.wektor)):
                    if self.wektor[i].show()[lista.index(item)] in item:
                        temp[lista.index(item)].append(self.wektor[i])
                        l += 1
                print(f'znaleziono {l} robotow bazujac na parametrze {item}')
        # print(temp[1][0].show())
        result = temp[0] + temp[1] + temp[2] + temp[3] + temp[4]
        final = list(set(result))

        if final:
            return final[0].show()
        else:
            return None


f2 = Flota()
f2.odczytaj_plik('roboty.txt')
f2.wyswietl()

print(f2.wyszukiwanie_lin(input('Podaj parametr: '), input('Podaj wartosc parametru: ')))
i = input('Podaj identyfikator: ')
t = input('Podaj typ: ')
m = input('Podaj mase: ')
z = input('Podaj zasieg: ')
r = input('Podaj rozdzielczosc: ')
if m:
    m = int(m)
if z:
    z = int(z)
if r:
    r = int(r)
print(f'Znaleziono robota: {f2.wyszukiwanie_zaaw(i, t, m, z, r)}')

# 3 podpunkt
i = []
t = []
m = []
z = []
r = []
print(i, t, m, z, r)
while True:
    ans = 1
    while ans:
        i.append(input('Podaj identyfikator: '))
    ans = 2
    while ans:
        t.append(input('Podaj typ: '))
    ans = 3
    while ans:
        ans = input('Podaj mase: ')
        m.append(int(ans) if ans else ans)
    ans = 4
    while ans:
        ans = input('Podaj zasieg: ')
        z.append(int(ans) if ans else ans)
    ans = 5
    while ans:
        ans = input('Podaj rozdzielczosc: ')
        r.append(int(ans) if ans else ans)
    break
print(i)

print(f'Znaleziono robota: {f2.wyszukiwanie_final(i, t, m, z, r)}')
print('przepraszam za spaghetti code \a')

