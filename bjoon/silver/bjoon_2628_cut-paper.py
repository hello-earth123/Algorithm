w, h = map(int, input().split())
n = int(input())

horizontal = [0, h]  # 가로 자르는 위치
vertical = [0, w]    # 세로 자르는 위치

for _ in range(n):
    d, num = map(int, input().split())
    if d == 0:
        horizontal.append(num)
    else:
        vertical.append(num)

horizontal.sort()
vertical.sort()

# 최대 높이
max_h = max(horizontal[i+1] - horizontal[i] for i in range(len(horizontal)-1))
# 최대 폭
max_w = max(vertical[i+1] - vertical[i] for i in range(len(vertical)-1))

print(max_h * max_w)