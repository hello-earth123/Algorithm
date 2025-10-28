import sys
input = sys.stdin.readline

S = set()
N = int(input())

for _ in range(N):
    order = input().strip().split()
    
    if order[0] == 'add':
        S.add(int(order[1]))
    
    elif order[0] == 'remove':
        S.discard(int(order[1]))  # remove보다 discard가 안전
    
    elif order[0] == 'check':
        sys.stdout.write('1\n' if int(order[1]) in S else '0\n')
    
    elif order[0] == 'toggle':
        x = int(order[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    
    elif order[0] == 'all':
        S = set(range(1, 21))
    
    elif order[0] == 'empty':
        S.clear()
