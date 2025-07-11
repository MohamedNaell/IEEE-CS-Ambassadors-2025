n = int(input())
arr = list(map(int, input().split()))

reversed_arr = []

for i in range(n - 1, -1, -1):
    reversed_arr.append(arr[i])

if arr == reversed_arr:
    print("YES")
else:
    print("NO")
