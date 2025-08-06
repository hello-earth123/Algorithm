width, height = map(int, input().split())
number_of_store = int(input())
coordinates = []

# 사각형을 펼친다.
# 북(1)에서 시작하면 2 * (width+height)에서 시작하여 역순으로 뒷숫자만큼 이동
# 남(2)에서 시작하면 +height에서 시작하여 뒷숫자만큼 앞으로
# 서(3)에서 시작하면 0에서 시작하여 뒷숫자만큼 앞으로
# 동(4)에서 시작하면 height*2+width 만큼 역순으로 뒷수자만큼 이동


# 상점 좌표 남기기
for _ in range(number_of_store):
    store_location = list(map(int, input().split()))
    coordinates.append(store_location)


# 동근이 좌표 남기기
dong_location = list(map(int, input().split()))


# 동근이 위치 수직선에 표시
for i in range(len(dong_location)):
    if dong_location[i] == 1: # 역순
        d = 2 * (width + height)

    elif dong_location[i] == 2:
        d = height

    elif dong_location[i] == 3:
        d = 0

    else:                     # 역순
        d = height * 2 + width


# 상점 좌표 수직선에 표시
for loc in coordinates:
    for x in loc:
        if x == 1:
            pass


# 빼기


# 결과