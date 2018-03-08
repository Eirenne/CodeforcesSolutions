N, K = (int(a) for a in input().split())
if K == N and N != 1:
    print(-1)
else:
    res = (N-1)/K
    if (N-1) % K != 0:
        res += 1
    print(int(res))

