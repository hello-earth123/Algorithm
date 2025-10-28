import sys
from collections import deque
input = sys.stdin.readline
stack = deque()

K = int(input())

for _ in range(K):
    N = int(input())

    if N == 0:
        stack.pop()
    else:
        stack.append(N)

print(sum(stack))
