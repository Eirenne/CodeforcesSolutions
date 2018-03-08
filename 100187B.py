import collections
s = str(input())
c = collections.Counter(s)
res = 0
for key,val in c.items():
    res += val*val

print(float(res)/len(s))