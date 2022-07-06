import random
import numpy as np
import statistics

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


r_num = 50
f1 = Flota()
f1.generuj_flote(r_num, 10)
f1.wyswietl()
print(f1.share(2))
H = 25


def hasz(robot, h):
    a = 0
    b = 0
    for j in robot[0]:
        a += ord(j)
    for k in robot[1]:
        b += ord(k)
    return (robot[2] + robot[3] * 2 + robot[4] ^ (a + b)) % h + 1


def robot_hasz(m, h):
    for i in range(m):
        print(f'Robot: {f1.share(i)} uzyskal wartosc: {hasz(f1.share(i), h)}')
        # print(hasz(f1.share(i), h))
        # print(f1.share(i))


robot_hasz(r_num, H)


def GWW(r, h):
    hassed = np.zeros(h)
    i = 0
    j = 0
    while True:
        hassed[i] = hasz(r[j], h)
        i += 1
        j += 1
        # print(hassed)
        if j == len(r):
            return hassed
        elif i == len(hassed):
            i = 0


table_of_robots = []
result_table = []
for i in range(r_num):
    table_of_robots.append(f1.share(i))
    result_table.append([f1.share(i), hasz(f1.share(i), H)])

print(GWW(table_of_robots, H))
for i in range(r_num):
    print(result_table[i])


def find_robot(params, robots, h_vector):
    wart = hasz(params, H)
    # print(wart)
    if wart in h_vector:
        for i in range(len(robots)):
            # print(robots[i][1])
            if wart == robots[i][1]:
                return robots[i][0]
    else:
        return None


print(find_robot(['EOOYFWMXLN', 'AGV', 1688, 113, 18], result_table, GWW(table_of_robots, H)))


def find_robot_mod(mass, rang, prec):
    results = []
    found = []
    for j in range(prec):
        x1 = ''
        for i in range(10):
            x1 += chr(random.randint(65, 90))
        t = random.choice(['AUV', 'AVF', 'AGV'])
        r = random.randint(1, 30)
        if not mass:
            mass = random.randint(50, 2000)
        if not rang:
            rang = random.randint(1, 1000)
        temp = [x1, t, mass, rang, r]
        results.append(hasz(temp, H))
        if find_robot(temp, result_table, GWW(table_of_robots, H)):
            found.append(find_robot(temp, result_table, GWW(table_of_robots, H)))
    return found


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    return num


print(most_frequent(find_robot_mod(1688, 113, 500)))
