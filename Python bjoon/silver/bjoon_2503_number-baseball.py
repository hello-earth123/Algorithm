# 영수 1~9 / 3개
# 민혁 1~9 / 3개

# 같은 자리면 strike / 존재하고 자리가 다르면 ball
# 3 stike 면 게임 종료
from itertools import permutations

T = int(input())

# 1~9 중 3자리 서로 다른 수
candidates = list(permutations(range(1, 10), 3))

# T개의 조건 입력
conditions = []
for _ in range(T):
    number, strike, ball = map(str, input().split())
    number = tuple(map(int, number))   # ex) "327" → (3,2,7)
    strike = int(strike)
    ball = int(ball)
    conditions.append((number, strike, ball))


# 입력 받은 모든 number, strike, ball을 만족해야하므로
# 하나라도 만족하지 못하면 탈락 (즉시 break)
# 다음 후보로 ㄱㄱ
answer = 0
for cand in candidates:
    ok = True
    for number, want_s, want_b in conditions:
        # 스트라이크 계산
        s_cnt = sum(1 for a, b in zip(cand, number) if a == b)
        # 볼 계산 (공통 원소 개수 - 스트라이크)
        b_cnt = len(set(cand) & set(number)) - s_cnt

        if s_cnt != want_s or b_cnt != want_b:
            ok = False
            break
    if ok:
        answer += 1

print(answer)
