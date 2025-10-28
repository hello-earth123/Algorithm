import sys
import heapq

lst = []
input = sys.stdin.readline

N = int(input())

# 순회하면서 최소값 출력 or 0 출력
for _ in range(N):
    number = int(input())
    
    if number == 0:
        if lst:
            print(heapq.heappop(lst))    
        else:
            print(0)
        
    else:
        heapq.heappush(lst, number)