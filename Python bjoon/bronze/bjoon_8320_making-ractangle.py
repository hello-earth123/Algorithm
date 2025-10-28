# 이동, 회전은 같은 직사각형으로 본다.
# 변형, 겹침은 불가능하다.
# 안에 빈 칸이 있으면 안된다.

n =  int(input())

# 약수 리스트
devisor = []

# 1은 무조건 포함이니까 시작
result = 0

for rec in range(1, n+1):
    devisor.clear()
    for number in range(1, rec+1):

        if rec % number == 0:
            devisor.append(number)
    
    # 약수 길이가 하나면 1만 있다는 뜻 -> 1이라는 뜻
    if len(devisor) == 1:
        result += 1

    # 약수 길이가 짝수개면 
    elif len(devisor) % 2 == 0:
        result += len(devisor) // 2

    else:
        result += (len(devisor) // 2) + len(devisor) % 2
    
print(result)


# 123456
# 1 -> 정사각형(그냥 블록 하나) 1개 만들 수 있음
# 12 -> 두 개 이어 붙여서 직사각형 1개 만들 수 있음
# 13 -> 세 개 이어 붙여서 직사각형 1개
# 124 -> 네 개 이어붙인거랑 두 개 짜리 세로로 이어 붙인 정사각형으로 총 2개
# 15 -> 다섯 개 이어붙인 직사각형 1
# 1236 2 -> 6개 이어붙인 직사각형이랑 두 개짜리 세 개 세로로 이어붙인 직사각형으로 총 2개
# 만약 약수의 길이가 1이면 1
# 만약 약수의 길이가 짝수이면 약수 갯수//2
# 만약 약수의 길이가 홀수이면 약수 갯수//2 + 약수 갯수%2 (몫과 나머지의 합)
