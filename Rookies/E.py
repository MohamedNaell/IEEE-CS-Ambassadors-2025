n = int(input())
arr = list(map(int, input().split()))

min_value = arr[0]
min_index = 0

for i in range(1, n):
    if arr[i] < min_value:
        min_value = arr[i]
        min_index = i

print(min_value, min_index + 1)
