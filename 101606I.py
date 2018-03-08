N = int(input())
settings = [int(a) for a in input().split()]
tree = int(input())
min = 4000
min_setting = 600
for setting in settings:
    if tree % setting < min:
        min = tree % setting
        min_setting = setting
print(min_setting)