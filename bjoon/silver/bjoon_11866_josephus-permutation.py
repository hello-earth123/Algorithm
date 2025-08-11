from collections import deque

N, K = map(int, input().split())
lst = list(range(1, N+1))
# print(lst)
queue = deque()
i = 0
while lst:
    # 원형 테이블을 순환시키는 방법
    # K-1은 인덱스 번호, i는 K만큼 증가하는 것을 표현, 원형의 형태로 순환하려면 리스트 길이로 나눈 나머지로 계속 순환한다.
    number = lst.pop(((K-1)+i)%len(lst))
    queue.append(number)
    i += K
    
print(queue)