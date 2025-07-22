#변수 두 개를 활용하여 누적 합을 형성할 수 있다.

N = int(input())

time = list(map(int, input().split()))
time.sort()  
time_sum = 0
row = 0 

for i in range(N):
    row += time[i]
    time_sum += row
    
print(time_sum)