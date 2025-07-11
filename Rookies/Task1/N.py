A, B = map(int, input().split())
S = input()

if len(S) == A + B + 1 and S[A] == '-' and S.replace('-', '').isdigit():
    print("Yes")
else:
    print("No")
