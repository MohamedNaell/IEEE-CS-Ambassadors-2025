n = int(input())

for _ in range(n):
    s, t = input().split()
    result = ""
    min_len = min(len(s), len(t))

    for i in range(min_len):
        result += s[i] + t[i]

    result += s[min_len:] + t[min_len:]

    print(result)
