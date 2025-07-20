from collections import deque

N=int(input())

q=deque(range(1,N+1))

while len(q)>1:
    q.popleft() #제일 왼쪽 카드 버리기
    q.append(q.popleft()) #뒤로 보내기
    
print(q[0])