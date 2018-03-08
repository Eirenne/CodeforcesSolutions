N, K = (int(a) for a in input().split())
L = [0] * N
a = 1
f = N - 1
while K > 0:
    if K > f:
        K -= f
        L[f] = a
        a += 1
        f -= 1
    else:
        L[K] = a
        a += 1
        break
for i in range(N):
    if L[i] != 0:
        print(L[i])
    else:
        print(a)
        a += 1
