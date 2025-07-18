N, Q = map(int, input().split())
S = list(input().strip())

for _ in range(Q):
    query = input().split()
    
    if query[0] == "pop_back":
        S.pop()
        
    elif query[0] == "front":
        print(S[0])
        
    elif query[0] == "back":
        print(S[-1])
        
    elif query[0] == "sort":
        l, r = map(int, query[1:3])
        S[l-1:r] = sorted(S[l-1:r])
        
    elif query[0] == "reverse":
        l, r = map(int, query[1:3])
        S[l-1:r] = S[l-1:r][::-1]
        
    elif query[0] == "print":
        pos = int(query[1])
        print(S[pos-1])
        
    elif query[0] == "substr":
        l, r = map(int, query[1:3])
        print(''.join(S[l-1:r]))
        
    elif query[0] == "push_back":
        x = query[1]
        S.append(x)