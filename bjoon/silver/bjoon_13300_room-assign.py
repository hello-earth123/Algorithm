
# S=0 Y=1 -> 1학년 여자
# S=0 Y=2 -> 2학년 여자
# S=0 Y=3 -> 3학년 여자
# S=0 Y=4 -> 4학년 여자
# S=0 Y=5 -> 5학년 여자
# S=0 Y=6 -> 6학년 여자
# S=1 Y=1 -> 1학년 남자
# .
# .
# .
# S=1 Y=6 -> 6학년 남자
room=0
count=0
N,K=map(int, input().split()) #학생 수

students=[]
for i in range(N):
    S,Y=list(map(int, input().split()))
    students.append((S,Y))
    for j in range(N):
        if students[i]==students[j]:
            count+=1
print(students[1])
#K를 넘어가면 몫+1
#K보다 작거나 같다면 1

if (count)>K:
    room=(count//K)+1
elif (count)<=K:
    room+=1
