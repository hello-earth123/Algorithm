# # f(n) = f(n-1) + f(n-2) (n>=2)
# # 피보나치 수

# def fibo(n):
#     if n == 2:
#         return 1
    
#     elif n == 1:
#         return 1
    
#     elif n == 0:
#         return 0
    
#     else:
#         return fibo(n-1) + fibo(n-2)
            
# print(fibo(int(input())))



memo = {0:0, 1:1, 2:1}


def fibo(n):
    if n in memo:
        return memo[n]
    
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]
print(fibo(int(input())))


# 1. 재귀만 쓴 피보나치 (중복 많음)
# fibo(n)을 부르면 fibo(n-1), fibo(n-2)를 다시 부르고

# fibo(n-1)은 다시 fibo(n-2), fibo(n-3)를 부르고…

# 이렇게 중복 호출이 기하급수적으로 늘어나서 시간 복잡도가 약 O(2^n) 이 됨.

# n	호출 횟수 (대략)
# 5	15
# 10	177
# 20	21,891
# 30	약 2백만
# 40	약 2십억

# 2. 메모이제이션 쓴 피보나치 (중복 제거)
# 각 fibo(i)는 한 번만 계산해서 결과를 저장함

# 이미 계산한 값은 저장소에서 바로 꺼내 써서 호출 횟수가 크게 줄음

# 시간 복잡도는 O(n)