def func(s):
    for i in range(len(s)):
        for j in range(i, len(s)):
            s1 = s[i:j + 1]
            if s1 == s1[::-1]:
                if len(s1) % 2 == 0:
                    print("Or not.")
                    return
    print("Odd.")


s = input()
func(s)


