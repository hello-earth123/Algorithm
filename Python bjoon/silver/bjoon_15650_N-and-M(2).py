N, M = map(int, input().split())

def recur(start, result):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, N):
        recur(i + 1, result + [arr[i]])
        
arr = list(range(1, N + 1))
recur(0, [])