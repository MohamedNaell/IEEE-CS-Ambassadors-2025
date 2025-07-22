def concatenate_arrays(a, b):
    c = b + a
    print(*c)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
concatenate_arrays(a, b)
