K = int(input())

W, H = map(int, input().split())

# 영역 생성
zone = []
for _ in range(H):
    row = list(map(int, input().split()))
    zone.append(row)

# 말 K번 반복하고 -> 원숭이 반복
# 반례가 존재함 -> 폐기
# 인접 영역에 1 이 발견되면 말 사용
# 반례가 존재함 -> 폐기

