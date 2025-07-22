def power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result

def calculate_equation(x, n):
    s = 0
    for i in range(n + 1):
        if i % 2 == 0:
            s += power(x, i)
    s -= 1
    print(s)

x, n = map(int, input().split())
calculate_equation(x, n)
