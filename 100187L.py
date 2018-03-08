s = list(input())

i = 0
l = len(s)
while i < int(l/2):
    s[i] = s[l-i-1]
    i += 1

print("".join(s))