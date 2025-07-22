def average(arr):
    total = 0
    for num in arr:
        total += num
    print(f"{total / len(arr):.6f}")

n = int(input())
arr = list(map(float, input().split()))
average(arr)
