inp1 = [int(a) for a in input().split()]
inp2 = [int(a) for a in input().split()]
inp3 = [int(a) for a in input().split()]

det = inp1[0] * (inp2[1]*inp3[2] - inp2[2]*inp3[1]) - inp1[1]*(inp2[0]*inp3[2] - inp2[2]*inp3[0]) + \
      inp1[2]*(inp2[0]*inp3[1] - inp2[1]*inp3[0])
print(det)
