N, A = (int(a) for a in input().split())

n_digits = len(str(A))
next_round = int("1" + n_digits*"0")
ans = 0
while 1:

    n_numbers = next_round - A
    if N < n_numbers:
        ans += N * n_digits
        break
    ans += n_numbers * n_digits

    A = next_round
    n_digits += 1
    next_round *= 10
    N -= n_numbers

print(ans)
