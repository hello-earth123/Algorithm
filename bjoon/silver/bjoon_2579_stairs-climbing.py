# 동적계획법
# - 최적해(최대값, 최소값)를 구하는 알고리즘
# - 큰 문제를 작은 문제로 나눈다.
# - 작은 문제의 최적해를 구한다
# - 작은 문제의 최적해들을 조합해서 큰 문제의 최적해를 구한다.

# ex) f(n) : n번 계단까지 갔을 때 최대값
#     p(n) : n번 계단의 점수
# 본래 구하고자 하는 문제 : f(6)
# 작은 문제: f(1), f(2), ...f(5)

# f(1) = 10
# f(2) = 10 + 20 = 30
# f(3) = (10 + 15) or (20 + 15) = 35
# f(4) = ....

# f(n) = (f(n-2) + p(n)) or (f(n-3) + p(n-1) + p(n))





# 계단 연속 세 개는 안됨
# 계단은 i+1 혹은 i+2로 뛸 수 있음
# 마지막 계단은 반드시 밟아야함

stair_number = int(input())
stairs = []

# 제일 마지막 부분에서 시작하여 거꾸로 가기(마지막은 무조건 가야하므로 도착 지점이 정해져 있음)
# 시작 지점은 점수가 0인 계단으로 만든다.


#계단 만들기
stairs += [0] # 시작 지점
for _ in range(stair_number):
    N = int(input())
    stairs.append(N)

# 시작 지점
i = len(stairs) - 1   # 6
count = 1
score = stairs[i] # 20

# 계단
while True:
    # 종료 조건
    if i == 1:
        break
    

    # 반복 조건
    # 계단 이동
    # 두 칸을 연속으로 갔다면 점프
    if count == 2:
        score += stairs[i-2]
        i -= 2
        count = 1
        
        
    # -1, -2 중 더 큰 계단 선택
    elif (stairs[i-1] > stairs[i-2]) and count < 2:
        score += stairs[i-1]
        i -= 1
        count += 1
        

    elif (stairs[i-1] <= stairs[i-2]) and count < 2:
        score += stairs[i-2]
        i -= 2
        count = 1

    # # 만약 둘이 같다면? 
    # elif (stairs[i-1] == stairs[i-2]) and count < 2:
        
    #     pass

print(score)



# 파리퇴치, 파리퇴치3 풀고 외우기
# 버블, 카운팅, 선택 정렬 암기
# min, max, sort등 내장함수 사용 x
# 알고리즘 시험환경 세팅하기