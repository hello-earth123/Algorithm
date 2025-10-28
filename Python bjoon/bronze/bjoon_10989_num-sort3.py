import sys

input=sys.stdin.readline
print=sys.stdout.write

N=int(input())

count=[0]*10001
for i in range(N):
    num=int(input())
    count[num]+=1

output=[]    
for i in range(1,10001):
    if count[i]:
        print((f"{i}\n") * count[i])
        
#메모리 제한이 있어서 파이썬으로는 못 푼다. -> 그래도 최대한 메모리, 시간을 줄이는 방법을 배움