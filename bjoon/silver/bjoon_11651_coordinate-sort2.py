N=int(input())
a=[]
for i in range(N):
    x,y=map(int, input().split())
    a.append([y,x])
a.sort()
for i in range(N):
    print(a[i][1],a[i][0])

