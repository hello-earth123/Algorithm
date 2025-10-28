N, M = map(int, input().split())
rolls = list(map(int, input().split()))

count = 0
ten_div = []
not_div = []

for r in rolls:
    if r == 10:
        count += 1  # 바로 카운트
    elif r % 10 == 0:
        ten_div.append(r)
    else:
        not_div.append(r)

# 길이 10의 배수 케이크 먼저 (자르기 쉬움)
ten_div.sort()

for cake in ten_div:
    pieces = cake // 10  # 만들 수 있는 10짜리 조각 수
    cuts_needed = pieces - 1  # 자를 횟수는 조각 수 - 1

    if M >= cuts_needed:
        M -= cuts_needed
        count += pieces
    else:
        count += M  # 더 이상 못 자르니 가능한 만큼만
        M = 0
        break

# 이제 10의 배수가 아닌 케이크 (자투리 생김)
if M > 0:
    for cake in not_div:
        pieces = cake // 10
        cuts_needed = pieces

        if M >= cuts_needed:
            M -= cuts_needed
            count += pieces
        else:
            count += M
            M = 0
            break

print(count)



# # 고른 롤케이크의 길이가 x
# # 0부터 x 사이에 있는 자연수 y
# # 롤케이크를 잘라서 y, x-y 두 개로 나눔
# # 롤케이크를 자를 수 있는 횟수는 M번
# # 10으로 만들 수 있는 최대값


# # N은 롤케이크의 갯수, M은 자를 수 있는 횟수
# N, M = map(int, input().split())

# roll_cake = list(map(int, input().split()))
# count = 0

# # 오름차순정렬
# roll_cake.sort()

# # 10의 갯수 세기
# for x in roll_cake:
#     if x == 10:
#         count += 1
    
# #백트래킹을 통해서 계속 순환(리스트를 벗어날 일이 없음 // 계속 순회함)
# # 10이 아닐 때
# for _ in range((M//N)):
#     for i in range(N-1, -1, -1):
            
#         if roll_cake[i] == 20:
#             roll_cake[i] = (roll_cake[i] - 20)
#             count += 2
            
#         elif roll_cake[i] > 10:
#             roll_cake[i] = (roll_cake[i] - 10)
#             count += 1

#         else:
#             continue

# # print(roll_cake)    
# print(count)