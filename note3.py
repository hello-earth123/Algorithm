N = int(input())
ramens = list(map(int, input().split()))
pay = 0

for i in range(N - 2):
    # 두 번째가 세 번째 보다 많다면 첫 번째와 두 번째를 묶기
    if ramens[i + 1] > ramens[i + 2]:
        t = min(ramens[i], ramens[i + 1] - ramens[i + 2])
        ramens[i] -= t
        ramens[i + 1] -= t
        pay += 5 * t
    
    # 아니면 무조건 세 개를 다 묶는게 베스트
    t = min(ramens[i], ramens[i + 1], ramens[i + 2])
    ramens[i] -= t
    ramens[i + 1] -= t
    ramens[i + 2] -= t
    pay += 7 * t

    # 묶어서 산 다음 첫 번째가 남아있다면 나머지 처리
    if ramens[i] > 0:
        pay += 3 * ramens[i]
        ramens[i] = 0

# 마지막 두 개는 세 개로 묶을 수 없기 때문에
# 마지막 두 개가 라면이 뭔가 남아 있다면 따로 처리
if ramens[N - 2] > 0 and ramens[N - 1] > 0:
    # 두 개로 묶을 수 있다면 반드시 묶어서 처리
    t = min(ramens[N -2], ramens[N - 1])
    pay += 5 * t
    ramens[N - 2] -= t
    ramens[N - 1] -= t

# 묶어서 처리한 후에 ramens[N - 2] 남 아 있다면 처리
if ramens[N - 2] > 0:
    pay += 3 * ramens[N - 2]

# 묶어서 처리한 후에 ramens[N - 1] 남 아 있다면 처리
if ramens[N - 1] > 0:
    pay += 3 * ramens[N - 1]
