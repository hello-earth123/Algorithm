# from pprint import pprint
R, C = map(int, input().split())

K = int(input())

# R = 7 / C = 6
# 공연장 생성
concert_hall = []
for _ in range(C):
    row = [0] * R
    concert_hall.append(row)
    
# concert_hall[C][0]에서 시작
# 시작 지점
nr = C-1
nc = 0


# 가다가 못가면 틀기 계속 반복
# 간 곳은 표시해놓기 0-> 1
# 사람 배치하면 한 명씩 줄이기 -> person > 0이 되면 0을 반환
person = K
# 상 -> 우 -> 하 -> 좌 반복
# 델타
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 시작 지점
concert_hall[nr][nc] = 1
person -= 1
count = 1

i = 0
while person > 0:
    # 다 찼는데 아직 person > 0 이면 0으로 만들고 break
    if count == R * C:
        break
    
    nr += dr[i%4]
    nc += dc[i%4]
    
    if (0 <= nr < C) and (0 <= nc < R) and (concert_hall[nr][nc] == 0):
        # 방문 표시
        concert_hall[nr][nc] = 1
        count += 1
        person -= 1
    else:
        nr -= dr[i%4]
        nc -= dc[i%4]
        i += 1

# pprint(concert_hall)

if person > 0:
    print(0)
else:
    print(nc+1, C - nr)