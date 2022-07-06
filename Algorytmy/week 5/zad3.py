import random

#a^b mod c
def szybki_pot_mod(a,b,c):
    d = 1
    b = bin(b)[2:][::-1] #miałem problem z kolejnością, łatwiej było odwrócić
    for i in range(len(b)-1,-1,-1):
        d = d**2 % c
        if b[i] == '1':
            d = (d*a) % c
        # print(i, b[i], d)
    return d


def test_fermana(p,n):
    q = [i for i in range(2,p)]
    for _ in range(n):
        choosed_q = random.choice(q)
        if szybki_pot_mod(choosed_q,p-1, p) != 1:
            return False

    return True

print(test_fermana(51,1000))


def test_millera_rabina(p,k):

    assert p > 1, p % 2 == 1

    t_r = 0

    while 2**t_r < p: #znajdywanie parametru r oraz q
        t_q = 1
        while ((2**t_r)*t_q) +1 < p:
            t_q +=1
        if ((2**t_r)*t_q) +1 == p:
            r = t_r
            q = t_q
        t_r += 1
    print(r,q)

    for _ in range(k): # powtarzanie czynności kilka razy
        a = random.randrange(2, p - 1)
        x = szybki_pot_mod(a, q, p)
        if x == 1 or x == p - 1:
            continue

        for _ in range(r - 1):
            x = szybki_pot_mod(x, 2, p)
            if x == p - 1:
                break
        else:
            return 'zlozona'
    return 'prawdopodobnie pierwsza'




print(test_millera_rabina(7,30))