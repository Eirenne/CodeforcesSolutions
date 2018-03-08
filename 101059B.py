N = int(input())
numbers = [int(a) for a in input().split()]
dict = {}
i = 0
while i < len(numbers):
    number = numbers[i]
    if number in dict:
        tup = dict[number]
        dict[number] = (tup[0], i, max(tup[2], i - tup[1] - 1))
    else:
        dict[number] = (i, i, 0)

    i += 1

ret = -1
for key, n in dict.items():
    m = max(n[2], n[0] + N - n[1] - 1)
    if m < ret or ret == -1:
        ret = m

ret += N
print(ret)

