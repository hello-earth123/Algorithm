N = int(input())

# 함수 생성
memo = [0] * 30001
def sub_fibo(n):
    global memo
    memo[0] = N
    memo[1] = n
    
    x = 1
    count = 2
    while memo[x] >= 0:   
        x += 1  
          
        if x >= 2:
            memo[x] = memo[x-2] - memo[x-1]
            
        if memo[x] >= 0:
            count += 1
        
    return count

# 최댓값과 그 때의 두 번째 숫자 찾기
result = float('-inf')
for number in range(1, 30001):
    if sub_fibo(number) > result:
        result = sub_fibo(number)
        num = number

# 출력        
print(result)

for idx in range(sub_fibo(num)):
    print(memo[idx], end = ' ')
print()