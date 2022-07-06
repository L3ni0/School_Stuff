import numpy as np
prime = []

def cz(p):
    global prime

    for i in range(2,int(np.sqrt(p))+1):
        if p % i == 0:
            prime.append(i)
            break
    else:
        prime.append(p)
        return
    cz(p//i) # ostatni dzielnik, jest to problematyczne jesli to dam do petli

cz(15)
print(prime)

def sera(p):
    x = [1 if i > 1 else 0 for i in range(p+1)]

    for n in range(2,int(np.sqrt(p))+1):
        if x[n] == 1:
            for j in range(2, p//n+1):
                x[n*j] = 0

    return x

print(sera(51))
x =sera(51)
print([i for i in range(len(sera(51))) if x[i]==1])