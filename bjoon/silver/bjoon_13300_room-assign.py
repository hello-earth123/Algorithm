N, K = map(int, input().split())

# 학생 
boys = []
girls = []
boys_counts = [0] * 7
girls_counts = [0] * 7
for _ in range(N):
    info = list(map(int, input().split()))
    if info[0] == 0:
        girls.append(info)
        
    else:
        boys.append(info)    

# print(boys)
# print(girls)

# 남학생 카운팅
for i in range(len(boys)):
    boys_counts[boys[i][1]] += 1
    
# 여학생 카운팅
for i in range(len(girls)):
    girls_counts[girls[i][1]] += 1
    
room = 0
for idx in range(1, len(boys_counts)):
    if boys_counts[idx] <= K and boys_counts[idx] != 0:
        room += 1
    
    else:
        if boys_counts[idx] % K == 0:
            room += (boys_counts[idx] // K)
        else:
            room += (boys_counts[idx] // K) + 1
        
for idx in range(1, len(girls_counts)):
    if girls_counts[idx] <= K and girls_counts[idx] != 0:
        room += 1
    
    else:
        if girls_counts[idx] % K == 0:
            room += (girls_counts[idx] // K)
        else:
            room += (girls_counts[idx] // K) + 1

print(room)