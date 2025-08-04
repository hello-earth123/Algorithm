number_of_paper = int(input())


# 도화지 생성
sheet = []
a = [0] * 100
width = []
height = []
circum = 0

for _ in range(100):
    sheet.append(a)


# 색종이 겉 둘레 구하기
for _ in range(number_of_paper):
    start_right, start_up = map(int, input().split())

    width.append(start_right)
    height.append(start_up)


    print(width)
    print(height)


    wid = max(width)+10-min(width)
    hei = max(height)+10-min(height)

    circum = wid * 2 + hei * 2


# 색종이 안에가 만약에 존재한다면 안둘레 구하기





#     for i in range(10):
#         for j in range(10):
#             sheet[(99-start_up)-i][(start_right-1)+j] += 1
#             area += 1


# for _ in range(1, number_of_paper+1):
#     if sheet != 1:
#         area -= 1 * (number_of_paper-1)

