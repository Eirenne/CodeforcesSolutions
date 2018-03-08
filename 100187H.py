

x1, y1 = (int(a) for a in input().split())
x2, y2 = (int(a) for a in input().split())
x3, y3 = (int(a) for a in input().split())
x4, y4 = (int(a) for a in input().split())
x5, y5 = (int(a) for a in input().split())
x6, y6 = (int(a) for a in input().split())


sides1 = [(x1 - x2)**2 + (y1-y2)**2,
            (x2 - x3)**2 + (y2-y3)**2,
            (x3 - x1)**2 + (y3-y1)**2]

sides2 = [(x4 - x5)**2 + (y4-y5)**2,
            (x5 - x6)**2 + (y5-y6)**2,
            (x6 - x4)**2 + (y6-y4)**2]
sides1.sort()
sides2.sort()
if sides1[0]*sides2[1] == sides1[1]*sides2[0] and sides1[0]*sides2[2] == sides1[2]*sides2[0]:
    print("YES")
else:
    print("NO")
