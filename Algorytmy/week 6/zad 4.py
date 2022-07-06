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

    def wyszukanie_przedzialu(self,przedział,param): #wersja pojedyńcza
        i = self.sort_wzgl_wart(param)
        min, max = przedział
        l = 0
        p = len(self.wektor) - 1
        while l <= p:
            s = (l+p) // 2
            print(''.join([f' k{i} ' if i != s else f"|k{i}|" for i in range(len(self.wektor))]))
            if min <= self.wektor[s].show()[i] <= max :
                return self.wektor[s].show()
            elif self.wektor[s].show()[i] < min:
                l = s+1
            else:
                p = s-1
        return None

    def wyszukanie_przedzialu_rek(self,przedział,param): #wersja pojedyńcza
        i = self.sort_wzgl_wart(param)
        min, max = przedział
        l = 0
        p = len(self.wektor) - 1

        def szukaj_index(indeksy):
            l, p = indeksy
            while l <= p:
                s = (l + p) // 2
                if min <= self.wektor[s].show()[i] <= max:
                    return s
                elif self.wektor[s].show()[i] < min:
                    l = s + 1
                else:
                    p = s - 1
            return None


        while l <= p:
            s = (l+p) // 2
            if min <= self.wektor[s].show()[i] <= max :
                sl,sp = s,s
                while (szukaj_index([l,sl]) or szukaj_index([s,p])):
                    temp_l = szukaj_index([l,sl])
                    temp_p = szukaj_index([s,p])
                    if temp_l == sl and temp_p == sp:
                        break
                    if temp_l:
                        sl = temp_l
                    if temp_p:
                        sp = temp_p

                return sl,sp
            elif self.wektor[s].show()[i] < min:
                l = s+1
            else:
                p = s-1
        return None


f1 = Flota()
f1.odczytaj_plik('roboty.txt')
print(f1.wyszukanie_przedzialu([100,500],'masa'))


min,max = [300,400]
wynik = f1.wyszukanie_przedzialu_rek([min,max],'zasieg')
f1.wyswietl()

print(wynik)



