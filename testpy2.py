# 학생 수 N명
# 그룹 세 개 (우수 / 보통 / 부진)
# 학생들 점수를 토대로 score1, score2 임의로 선정하여 나눔


# score2 이상 -> 우수
# score1 이상 ~ score2 미만 -> 보통
# score1 미만 -> 부진

# 각 반별로 min과 max 사이(이상, 이하)를 만족

# 학생이 가장 많은 분반과 적은 분반의 학생 수 차의 최솟값은?
# min max를 만족하는 기준인 score1, score2가 없다면 -1을 출력

# 그런 점수가 없다면 -1을 반환한다.

# 모든 경우의 수를 다 만든 다음 -> 조건에 맞는 것들을 검사 -> 그 중에서 최소, 최대값을 구한다.


T = int(input())

for test_case in range(1, T+1):
    # N => 학생수 / minimum => 최소 인원 / maximum => 최대 인원
    N, minimum, maximum = map(int, input().split())

    # 분반 리스트
    

    # 학생들 점수
    scores = list(map(int, input().split()))
    
    r = float('inf')
    # score1, score2를 설정
    for score1 in range(1, 100):
        for score2 in range(score1+1, 101):
            best = []
            normal = []
            worst = []

            
            # 분반
            for score in scores:
                if  score >= score2:
                    best.append(score)

                elif score < score1:
                    worst.append(score)

                else:
                    normal.append(score)

            # print(best)
            # print(worst)
            # print(normal)

            # 학생 수 구하기
            max_class = max(len(best), len(normal), len(worst))
            min_class = min(len(best), len(normal), len(worst))
            result = (max_class - min_class)
            if minimum <= max_class <= maximum and minimum <= min_class <= maximum:
                if result < r:
                    r = result
    
    if r == float('inf'):
        print(f'#{test_case} {-1}')
    else:
        print(f'#{test_case} {r}')


