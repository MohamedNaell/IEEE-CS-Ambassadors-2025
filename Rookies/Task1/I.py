T = int(input())

for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    smallest = 1000000000

    for i in range(N):
        for j in range(i + 1, N):
            total = A[i] + A[j] + (j - i)

            if total < smallest:
                smallest = total

    print(smallest)
