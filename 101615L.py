import math
K, P, X = [int(a) for a in input().split()]
M = math.sqrt((K*P)/X)
lower = math.floor(M)
higher = math.ceil(M)
print("%.3f" % min(K*P/lower + lower*X, K*P/higher + higher*X))
