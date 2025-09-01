# 명령어 D S L R 이용하는 계산기
# 0 ~ 9999 저장 가능
# 저장된 숫자를 변환
# 숫자 d1 d2 d3 d4
# D -> (n * 2) 만약 10000이상이면 (n * 2) % 10000
# S -> n -1 만약 0이면 9999
# L -> rotate 반시계 방향 rotate(-1)
# R -> rotate 시계 방향 rotate(1)
# 주어진 A를 B로 바꾸는 최소 명령어
from collections import deque
T = int(input())

for _ in range(T):
    A, B = input().split()
    s = A.zfill(4)
    e = B.zfill(4)
    start = int(s)
    end = int(e)
    visited = [False] * (10000) # 상태는 현재의 숫자 (0~9999까지)
    queue = deque([start, dslr])
    visited[start] = True
    dslr = ['D', 'S', 'L', 'R']
    
    while queue:
        state = queue.popleft()
        if state == B:
            break
        
        for i in dslr:
            
            if dslr[i] == 'D':
                if state > 9999:
                    state %= 10000
                else:
                    state *= 2
                    
            if dslr[i] == 'S':
                state -= 1
            
            if dslr[i] == 'L':
                s_L = deque(str(state))
                s_L.rotate(-1)
                state = s_L
            
            if dslr[i] == 'R':
                s_R = deque(str(state))
                s_R.rotate(1)
                state = s_R
