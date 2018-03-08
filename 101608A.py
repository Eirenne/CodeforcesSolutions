with open("tabs.in","r") as f:
    lines = f.readline()
    for i in range(1, len(lines)):
        n , k = [int(a) for a in lines[i]]
        if n == 1:
            print("0")
        elif k == 1 or k == n:
            print("1")
        else:
            print("2")