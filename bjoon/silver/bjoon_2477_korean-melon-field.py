K = int(input())

# 방향 길이 순서
# 동 = 1, 서 = 2, 남 = 3, 북 = 4


# 주어진 조건을 가지고 넓이를 구해야한다.
# 사각형을 만드는 조건
# 4 -> 2 / 3 -> 1 / 4 -> 1 순서로 꺾는다면 사각형의 width, height가 구해짐
# 계단 식이면 3 -> 1 , 3 -> 1 형태가 두 번 반복됨
# 육각형이면 6번 반복이 고정
# 인덱스 번호가 하나만 있는 곳이 전체 사각형의 넓이
# 번호가 두 개 있는 곳은 나눠진건데 -> 양 끝 두 개를 곱한다.
# 사각형 넓이 구하기

# 제일 큰 값이 큰 사각형의 가로
# 큰 사각형의 넓이 (1번 리스트 * 3번 리스트) or (2번 리스트 * 4번 리스트)

# 사각형 그리는 순서
square = []
for _ in range(6):
    sides = list(map(int, input().split()))
    square.append(sides)

print(square)
# 각 리스트의 앞 숫자가 1, 2이면 가로
# 각 리스트의 앞 숫자가 3, 4면 세로
max_width = 0
max_height = 0
for lst in square:
    # 가로 최대 길이 구하기
    if lst[0] == 1 or lst[0] == 2:
        width = lst[1]
        if max_width < width:
            max_width = width
    # 세로 최대 길이 구하기
    else:
        height = lst[1]
        if max_height < height:
            max_height = height

# print(max_height)
# print(max_width)   

# 큰 사각형 넓이 구하기 
big_area = max_width * max_height

# 작은 사각형 넓이 구하기
small_height = 0
small_width = 0
for idx in range(len(square)):
    if square[idx][1] == max_width:
        small_height = abs(square[(idx-1)%6][1] - square[(idx+1)%6][1])
    
    if square[idx][1] == max_height:
        small_width = abs(square[(idx-1)%6][1] - square[(idx+1)%6][1])

small_area = small_width * small_height

area = big_area - small_area

print(area * K)