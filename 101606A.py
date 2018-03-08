N = int(input())

settlements = []
for i in range(N):
    settlements.append([int(a) for a in input().split()])

times = []
max_day = 0
for x in settlements:
    st = ""
    if x[1] < x[2]:
        st += "n"*(x[1] + 1)
        st += "d"*(x[2] - x[1] - 1)
        st += "n"*(x[0] - x[2])
    else:
        st += "d" * (x[2])
        st += "n" * (x[1] - x[2] + 1)
        st += "d" * (x[0] - x[1] - 1)
    times.append(st)
    if len(st) > max_day:
        max_day = len(st)

j = 0
imp = False
while 1:
    if j / max_day >= 1825:
        imp = True
        break
    all_night = True
    for time in times:
        if time[j % len(time)] == "d":
            all_night = False
            break
    if all_night:
        print(j)
        break
    j += 1

if imp:
    print("impossible")

