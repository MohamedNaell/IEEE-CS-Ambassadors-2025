n = int(input())
arr = list(map(int, input().split()))

min_element = min(arr)
count = arr.count(min_element)

if count % 2 == 1:
    print("Lucky")
else:
    print("Unlucky")