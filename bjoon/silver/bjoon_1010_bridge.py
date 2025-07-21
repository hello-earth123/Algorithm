import math
T=int(input())

for i in range(T):
    N,M=list(map(int, input().split()))
    print(math.comb(M,N))