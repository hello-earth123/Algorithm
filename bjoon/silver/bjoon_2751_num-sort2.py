import sys

N=int(input())
t=[]
for i in range(N):
   a=int(sys.stdin.readline())
   t.append(a)
t.sort()


for i in range(N):
    print(t[i])
# sys.stdout.write('\n'.join(map(str, t))) -> 이렇게 표한할 수도 있다.