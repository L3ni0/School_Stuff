from math import floor, ceil,sqrt

def ciag1(n:int):
    assert n > 0

    def x(n):
        if n==0:
            return 0
        else:
            return 3**n + x(n-1)

    return x(n)

def ciag2(n:int):
    assert n > 0

    def x(n):
        if n==-1 or n==0:
            return 0
        else:
            return n + x(n-2)

    return x(n)

def ciag3(n:int):
    assert  n > 1

    def x(n):
        if n==1:
            return 1
        elif n==0:
            return 0
        else:
            return x(n-1) + x(n-2)

    return x(n)


# 1.2

def ciag1_analityczny(n):
    return (3**(n+1)-3)/2


def ciag2_analityczny(n):
    return int(floor((n+1)/2) * ceil((n+1)/2))

def ciag3_analityczny(n):
    return int((1/sqrt(5))*(((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n))

## 1.3
n = 20

for i in range(1,n+1):
    print(ciag1(i), ciag1_analityczny(i), ciag1(i)==ciag1_analityczny(i))

print(20*'-')
for i in range(1,n+1):
    print(ciag2(i), ciag2_analityczny(i), ciag2(i)==ciag2_analityczny(i))


print(20 * '-')
for i in range(2,n+1):
    print(ciag3(i), ciag3_analityczny(i), ciag3(i)==ciag3_analityczny(i))
