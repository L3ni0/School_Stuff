N = [90, 103, 114]
P = [62, 72, 95]
S = [3.12, 3.49, 5.12]
T = []
for n,p,s in zip(N, P, S):
    t = n/p
    T.append(t)

X = []
minimum = max(T)
i = 0
for n,p,s,t in zip(N, P, S, T):
    print(t)
    if 1*t < minimum:
        X = [1 if i==l else 0 for l in range(len(N))]
        minimum = t
    i += 1


print(X)