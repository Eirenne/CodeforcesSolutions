N = int(input())
notes = [int(a) for a in input().split()]

ans = 0.0
for note in notes:
    if note == 0:
        ans += 2.0
    else:
        ans += 1.0/float(note)

print(ans)