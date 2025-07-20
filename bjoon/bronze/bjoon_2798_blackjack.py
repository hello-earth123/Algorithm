import sys

input=sys.stdin.readline
N,M=map(int, input().split())
a=input().split()
p=0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            temp=int(a[i])+int(a[j])+int(a[k])
            if temp<=M:
                if temp>p:
                    p=temp
                    
print(p)


    