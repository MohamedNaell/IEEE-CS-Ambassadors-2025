s = list(input().strip())
costs = list(map(int, input().strip().split()))
n = len(s)

def get_cost(c):
    return costs[ord(c) - ord('a')]

for i in range(n):
    if s[i] == '?':
        min_cost = float('inf')
        best_char = 'a'
        for j in range(26):
            c = chr(ord('a') + j)
            temp_cost = 0
            if i > 0 and s[i-1] != '?':
                temp_cost += abs(get_cost(c) - get_cost(s[i-1]))
            if i < n - 1 and s[i+1] != '?':
                temp_cost += abs(get_cost(c) - get_cost(s[i+1]))
            if temp_cost < min_cost:
                min_cost = temp_cost
                best_char = c
        s[i] = best_char

total_cost = 0
for i in range(n - 1):
    total_cost += abs(get_cost(s[i]) - get_cost(s[i+1]))

print(total_cost)
print("".join(s))
