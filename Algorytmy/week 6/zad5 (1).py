import random
from collections import OrderedDict
random.seed(100)


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

    def share(self, index):
        return self.wektor[index].show()

    def binary_search(self, param, wart, wektor):
        l = 0
        p = len(wektor) - 1
        while l <= p:
            s = (l + p) // 2
            # print(''.join([f' k{i} ' if i != s else f"|k{i}|" for i in range(len(wektor))]))
            # print(wektor[s][param], wart)
            if wektor[s][param] == wart:
                return wektor[s]

            elif wektor[s][param] < wart:
                l = s + 1
            else:
                p = s - 1
        return None


r_num = 20
f1 = Flota()
f1.generuj_flote(r_num, 10)
f1.wyswietl()


def Convert(i, t, m, z, r):
    d = {'id': i, 'typ': t, 'masa': m, 'zasieg': z, 'rez': r}
    return d


def pomoc(n, sort_by):
    listed = []
    result = []
    for i in range(n):
        # print(Convert(f1.share(i)[0], f1.share(i)[1], f1.share(i)[2], f1.share(i)[3], f1.share(i)[4]))
        listed.append(Convert(f1.share(i)[0], f1.share(i)[1], f1.share(i)[2], f1.share(i)[3], f1.share(i)[4]))
    newlist = sorted(listed, key=lambda d: d[sort_by])
    for i in range(n):
        result.append(list(newlist[i].values()))

    return result


def searching(l_p, i=None, t=None, m=None, z=None, r=None):
    # print(type(m), type([]))
    t1 = []
    t2 = []
    t3 = []
    t4 = []
    t5 = []
    if i:
        if isinstance(i, list):
            # print('yes')
            for j in i:
                t1.append(f1.binary_search(0, j, pomoc(l_p, 'id')))
        else:
            t1.append(f1.binary_search(0, i, pomoc(l_p, 'id')))
    if m:
        if isinstance(m, list):
            # print('yes')
            for j in m:
                t3.append(f1.binary_search(2, j, pomoc(l_p, 'masa')))
        else:
            # print(f1.binary_search(2, m, pomoc(l_p, 'masa')))
            t3.append(f1.binary_search(2, m, pomoc(l_p, 'masa')))
    if t:
        if isinstance(t, list):
            # print('yes')
            for j in t:
                t2.append(f1.binary_search(1, j, pomoc(l_p, 'typ')))
        else:
            t2.append(f1.binary_search(1, t, pomoc(l_p, 'typ')))
    if z:
        if isinstance(z, list):
            # print('yes')
            for j in z:
                t4.append(f1.binary_search(3, j, pomoc(l_p, 'zasieg')))
        else:
            t4.append(f1.binary_search(3, z, pomoc(l_p, 'zasieg')))
    if r:
        if isinstance(r, list):
            # print('yes')
            for j in r:
                t5.append(f1.binary_search(4, j, pomoc(l_p, 'rez')))
        else:
            t5.append(f1.binary_search(4, r, pomoc(l_p, 'rez')))
    t = t1 + t2 + t3 + t4 + t5
    t.remove(None)
    if t:
        return [ii for n, ii in enumerate(t) if ii not in t[:n]]
    else:
        return None


# szukaj_po = input('Po czym sortowac?: ')
# m = pomoc(20, szukaj_po)
# szukana = input("wpisz wartosc do szukania: ")
# print(m)
# print(f'Znaleziono robota: {f1.binary_search(2, int(szukana) if szukaj_po not in ["id", "typ"] else szukana, m)}')

print(searching(r_num, m=1688, t=['AGV', 'AFV'], r=[1, 3, 1]))
