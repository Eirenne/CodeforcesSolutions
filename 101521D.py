N = int(input())
sum1 = 0
sum2 = 0
x1 = 0
num1 = 0
num2 = 0
x2 = 0
for i in range(N):
    k = input()
    if k == "M":
        continue
    if k == "X":
        sum1 += 10
        num1 += 1
        x1 += 1
    elif k == "10":
        sum1 += 10
        num1 += 1
    else:
        sum1 += int(k)

for j in range(N):
    k = input()
    if k == "M":
        continue
    if k == "X":
        sum2 += 10
        num2 += 1
        x2 += 1
    elif k == "10":
        sum2 += 10
        num2 += 1
    else:
        sum2 += int(k)

if sum1 > sum2:
    print("Yuju")
elif sum2 > sum1:
    print("Yerin")
else:
    if num1 > num2:
        print("Yuju")
    elif num1 < num2:
        print("Yerin")
    else:
        if x1 > x2:
            print("Yuju")
        elif x2 > x1:
            print("Yerin")
        else:
            print("Shoot-off")
