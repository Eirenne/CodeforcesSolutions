N, M = (int(a) for a in input().split())
arr = []
for i in range(M):
    arr.append([int(a) for a in input().split()])


sorted_arr = sorted(arr, key=lambda a: a[1])
last_item = None
b = True
blockage = -1
for key, item in enumerate(sorted_arr):

    if last_item is None:
        if item[0] == 1:
            if (item[1] - 1) % 2 == 0:
                if (N - item[1] + 1) * 2 != M:
                    print("No")
                    b = False
                break
        else:
            if (item[1] - 1) % 2 == 1:
                if (N - item[1] + 1) * 2 != M:
                    print("No")
                    b = False
                break
        last_item = item
        M -= 1
        continue
    if item[0] == last_item[0]:
        if (item[1]-last_item[1]) % 2 == 0:
            if (N -item[1] + 1)*2 != M:
                print("No")
                b = False
            break
    else:
        if (item[1] - last_item[1]) == 0:
            if (N - item[1] + 1) * 2 - 1 != M:
                print("No")
                b = False
            break
        elif (item[1] - last_item[1]) == 1:
            if (N - item[1] + 1) * 2 != M:
                print("No")
                b = False
            break
        elif (item[1]-last_item[1]) % 2 == 1:
            if (N -item[1] + 1)*2 != M:
                print("No")
                b = False
            break
    last_item = item
    M -= 1

if b:
    print("Yes")
