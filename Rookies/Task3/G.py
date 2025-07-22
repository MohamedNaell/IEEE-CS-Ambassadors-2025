def find_min_max(arr):
    minimum = arr[0]
    maximum = arr[0]
    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    print(minimum, maximum)

n = int(input())
arr = list(map(int, input().split()))
find_min_max(arr)
