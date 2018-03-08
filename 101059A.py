p1 = int(input())
p2 = int(input())
p3 = int(input())
W = int(input())

if p1 + p3 >= W or p1 + p2 >= W or p2 + p3 >= W:
    print("YES")
else:
    print("NO")
