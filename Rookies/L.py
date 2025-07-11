T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    result = []

    for i in range(n):
        current_max = arr[i]
        for j in range(i, n):
            current_max = max(current_max, arr[j])
            result.append(current_max)
    
    print(*result)
