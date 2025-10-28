t=[]
total=0
for i in range(5):
   N=int(input())
   t.append(N) 
t.sort()  # 정렬
for i in range(5):
    total+=t[i]

print(int(total/5))
print(t[2])  # 중간값 출력