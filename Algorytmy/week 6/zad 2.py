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

    #do zadania 2
    def sort_wzgl_wart(self,param): #zwykły sort nie zadziałałby na klasach
        if param == 'masa':
            i = 2
        elif param == 'zasieg':
            i = 3
        elif param == 'rozdzielczosc':
            i = 4
        else:
            raise NameError(f'robot nie posiada parametru {param}')

        for k in range(1,len(self.wektor)): #zwykly ubblesort
            for p in range(len((self.wektor))-k):
                if self.wektor[p].show()[i] > self.wektor[p+1].show()[i]:
                    self.wektor[p], self.wektor[p+1] = self.wektor[p+1], self.wektor[p]

        return i

    def wyszukanie_binarne(self,wartosc,param): #wersja pojedyńcza
        i = self.sort_wzgl_wart(param)
        l = 0
        p = len(self.wektor)-1
        while l <= p:
            s = (l+p) // 2
            print(''.join([f' k{i} ' if i != s else f"|k{i}|" for i in range(len(self.wektor))]))
            if self.wektor[s].show()[i] == wartosc:
                return s
            elif self.wektor[s].show()[i] < wartosc:
                l = s+1
            else:
                p = s-1
        return None

    def wyszukanie_binarne_kilkukrotne(self,wartosci,param): #wersja pojedyńcza
        odpowiedzi = []
        for wart in wartosci:
            print(f'wyszukiwanie {wart}')
            if self.wyszukanie_binarne(wart,param):
                odpowiedzi.append(self.wektor[self.wyszukanie_binarne(wart,param)].show())
            print()

        return odpowiedzi


f1 = Flota()
f1.odczytaj_plik('roboty.txt')
# print(f1.wyszukanie_binarne(95, 'zasieg'))
# f1.wyswietl()
print(f1.wyszukanie_binarne_kilkukrotne([688,94],'masa'))
