import collections

T = int(input())
c = collections.Counter()
for i in range(T):
    N = int(input())
    c.clear()
    for j in range(N):
        name, freq = (a for a in input().split())
        c[freq] += 1

    print(sorted(c.items(), key=lambda el: (-el[1], el[0]))[0][0])
