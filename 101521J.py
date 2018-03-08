h,w = [int(a) for a in input().split()]
h1,w1 = [int(a) for a in input().split()]
h2,w2 = [int(a) for a in input().split()]


if h1 > h or w1 > w:
    print("No")
    print("No")
else:
    if h2 > h or w2 > w:
        print("No")
        print("Yes")
    else:
        if h-h1 >= h2 or w-w1 >= w2:
            print("Yes")
        else:
            print("No")

        if (h-h1)/2 < h2 and (w-w1)/2<w2:
            print("Yes")
        else:
            print("No")