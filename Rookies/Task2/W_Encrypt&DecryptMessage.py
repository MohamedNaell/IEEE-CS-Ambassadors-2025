Q = int(input())
S = input()

key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"
original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

if Q == 1:
    mapping = dict(zip(original, key))
else:
    mapping = dict(zip(key, original))

result = "".join(mapping[c] for c in S)
print(result)
