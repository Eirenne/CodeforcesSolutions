
T = int(input())
words = ["First", "Second", "Third"]
for i in range(T):
    l = [int(a) for a in input().split()]
    print(words[min(range(len(l)), key=l.__getitem__)])