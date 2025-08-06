width, height = map(int, input().split())
number_of_store = int(input())
coordinates = []
store_loc = []

# 사각형을 펼친다.
# 북(1)에서 시작하면 2 * (width+height)에서 시작하여 역순으로 뒷숫자만큼 이동
# 남(2)에서 시작하면 +height에서 시작하여 뒷숫자만큼 앞으로
# 서(3)에서 시작하면 0에서 시작하여 뒷숫자만큼 앞으로
# 동(4)에서 시작하면 height*2+width 만큼 역순으로 뒷수자만큼 이동


# 상점 좌표
for _ in range(number_of_store):
    store_location = list(map(int, input().split()))
    coordinates.append(store_location)


# 동근이 좌표
dong_location = list(map(int, input().split()))


# 동근이 위치 수직선에 고정
i=0
if dong_location[i] == 1: # 역순
    d = 2 * (width + height)
    d -= dong_location[i+1]
        
elif dong_location[i] == 2:
    d = height
    d += dong_location[i+1]
        
elif dong_location[i] == 3:
    d = 0
    d += dong_location[i+1]
        
else:                     # 역순
    d = height * 2 + width
    d -= dong_location[i+1]
        

# 상점 좌표 수직선에 표시
for loc in coordinates:
    x=0
    if loc[x] == 1: # 역순
        s = 2 * (width + height)
        s -= loc[x+1]
            
        
    elif loc[x] == 2:
        s = height
        s += loc[x+1]
            
        
    elif loc[x] == 3:
        s = 0
        s += loc[x+1]
        
    else:           # 역순
        s = height * 2 + width
        s -= loc[x+1]
            
    store_loc.append(s)

# '최단'(min) '거리'(abs) 계산
total = 0
for idx in range(len(coordinates)):
    total += min(abs(d - store_loc[idx]), (2*(height+width))-abs(d - store_loc[idx]))


# 결과
print(total)