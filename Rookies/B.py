n = int(input())
arr = list(map(int, input().split()))
x = int(input())

found = -1

for i in range(n):
    if arr[i]==x:
        found = i
        break

print(found)