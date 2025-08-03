from pprint import pprint

number_of_paper = int(input())

lst = []


# 도화지 생성 
for _ in range(100):
    lst.append([0] * 100)


# 색종이 총 넓이
area = 0

# 색종이 넓이 리스트에 추가하기 
for _ in range(number_of_paper):
    
    left, down = map(int, input().split())
    
    # lst[left-1][99-down] 이게 처음 (왼쪽 아래 꼭지점)
    # lst[left-1+10][99-(down)-10] 이게 마지막 (오른쪽 위에 꼭지점)
    
    
    # 겹치는거 까지 다 포함해서 색종이 전체 넓이 
    for i in range(10):
        for j in range(10):
            # 배열에 1씩 더하기 (왜? 영역 안에 배열의 갯수가 곧 넓이이기 때문에)
            lst[(99-down)-i][(left-1)+j] += 1
            
            # 넓이 저장할 변수
            area += 1
            
      
# 겹치는 부분 제거하기 ((겹치는 횟수-1) 만큼 전체 총 넓이에서 빼기)
for row in lst:
    for k in row:
        if k >= 2:
            area -= (k-1)
            
            
print(area)