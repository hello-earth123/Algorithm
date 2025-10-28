N=int(input())

members=[]
for i in range(N):
    a,b=map(str, input().split())
    members.append((int(a), b))

members.sort(key=lambda x:x[0])

for i in range(N):
    print(members[i][0], members[i][1])