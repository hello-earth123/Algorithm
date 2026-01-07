# 등차수열인 경우 -> 한수
# N 이하의 자연수에서 한수의 갯수 출력
N = int(input())
count = 0

# 모든 N 이하의 자연수 순회
for n in range(1, N + 1):
    if len(str(n)) == 1 or len(str(n)) == 2:    # 한자리 수 인 경우 모두 한수로 취급
        count += 1
    else:
        number = list(str(n))    # 자릿수 찢기
        flag = True
        
        for index in range(len(number) - 2):   # 완전 탐색 순회 (공차 비교)
            sub = int(number[index]) - int(number[index + 1])
            sub_2 = int(number[index + 1]) - int(number[index + 2])

            if sub != sub_2:
                flag = False
        if flag:
            count += 1
print(count)