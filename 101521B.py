a, b, c = [int(a.replace(".", "")) for a in input().split()]
if (a*b + a*c + b*c) < (a*b*c)/100:
    print("Yes")
else:
    print("No")