N=int(input())
t=list(map(float, input().split()))

new_t=[]
result=0
for i in range(N):
    new_t.append((t[i]/max(t))*100)
     
for x in range(N):
    result+=new_t[x]

print(result/N)