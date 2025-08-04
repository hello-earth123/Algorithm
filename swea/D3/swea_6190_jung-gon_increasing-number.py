def is_increasing(n):
    last_digit = float('inf')  # 어떤 숫자보다 큼 (0~9보다 큰 숫자) -> 1의 자리는 맨 처음 자릿수 이므로 무조건 통과시키기 위해
    while n > 0:
        current = n % 10

        if current > last_digit:
            return False
        
        last_digit = current # 앞으로 땡기기

        n =  n // 10 #자릿수 하나 앞으로
    return True

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())

    numbers = list(map(int, input().split()))

    max_danjo = -1


    for i in range(N - 1):
        for j in range(i + 1, N):
            mul_number = numbers[i] * numbers[j]

            if is_increasing(mul_number):
                if mul_number > max_danjo:
                    max_danjo = mul_number


    print(f'#{test_case} {max_danjo}')


    # 자릿수 비교를 위해서 먼저 10으로 나눈다. -> 그럼 몫과 나머지가 나오는데 몫이 다음 타겟, 나머지는 현재값
    # 현재값이 과거 값이 되고, 몫이 다시 10으로 나눌 숫자가 된다.


# T = int(input())


# for test_case in range(1, T+1):
#     multiply_list = []
#     danjo = []
#     result = 0

#     N = int(input()) # 숫자 갯수 N 

#     X = list(map(int, input().split())) # 주어지는 숫자들


#     # 숫자들을 자릿수별로 찢어서 리스트에 append하고 -> 상위 리스트에 append
#     for i in range(N-1):
#         for j in range(i+1, N):
#             multiply_number = X[i] * X[j]
#             multiply_list.append(multiply_number)


#     #각 자릿 수 별로 비교
#     for number in multiply_list:
#         res = True
#         i = 0   # 자릿수

#         if len(number) == 1:
#             continue

#         if (number // 10**i) >= (number // 10**(i+1)):  #자릿수 비교
#             i += 1  # 자릿수 하나씩 늘리기
#             continue
#         else:
#             res = False
        

#     #단조 판별
#     if res == True:
#         danjo.append(number)
    
#     if danjo:
#         result = max(danjo)
#     else:
#         result = -1

#     print(f'#{test_case} {result}')



    # # 단조 숫자를 만족한다면 T/ 아니면 F / danjo 리스트에 append
    # for p in multiply_list:

    #     res = True
    #     if len(p) == 1:
    #         danjo.append(int(p[0]))
    #         continue
        
    #     for i in range(len(p)-1):
    #         if int(p[i]) <= int(p[i+1]): # 지금 현재 p는 문자열을 가지고 있는 리스트이다.
    #             continue
    #         else:
    #             res = False

    #     if res == True:
    #         danjo.append(int(''.join(p)))


    # if danjo:
    #     result = max(danjo)  
    # else:
    #     result = -1

    #print(f'#{test_case} {result}')