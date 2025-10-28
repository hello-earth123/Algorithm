# 번호 부여 -> 키가 가장 작은 아이가 1번 ~~ 가장 큰 아이가 20번
# 학생 수는 항상 20명
# 겹치는 키는 한 명도 없음



# 아무나 한 명 뽑아 줄 맨 앞에 세움
# 다음 학생은
    # 자기 앞에 자기보다 큰 사람이 없으면 그대로
    # 만약 자기보다 큰 사람이 한 명 이상 있으면, 그 중 가장 앞에 있는 학생의 바로 앞에 선다. 
        # 그리고 인덱스 밀림 
        # -> 밀린 인덱스 총 합은???

# -> 밀린 인덱스 총 합은???


T = int(input())

for _ in range(T):

    height = list(map(int, input().split()))
    line_up = []
    test_case = height.pop(0)
    result = 0
    # print(tc)
    # print(height)

    # 아무나 한 명 추가


    for i in range(20):
        # 현재값
        current = height[i]


        # 처음에 아무나 넣기
        if not line_up:
            line_up.append(height[i])
            continue
        

        # 라인업 순회하면서 삽입 위치 찾기
        for j in range(len(line_up)):
            if current < line_up[j]:
                result += len(line_up) - j # 순회를 얼만큼 했느냐가 current 수의 크기를 결정하는셈
                line_up.insert(j, current) # 
                break
        
        # 아무도 큰 사람 없으면 그냥 뒤에 append
        else:
            line_up.append(current)



    print(f'{test_case} {result}')




            # # 만약 큰 사람이 아무도 없다면
        # if max(line_up) <= height[i]: 
        #     line_up.append(height[i])


        # # 만약 큰 사람이 있다면 그 중에 제일 작은 사람 뒤에 선다.
        # else: # 그게 아닌 모든 경우에 대해서
        #     # line_up 중에서 height[i] 보다 큰 사람 중에 가장 작은 사람의 인덱스에
        #     line_up.insert(line_up.index(min(line_up)), height[i])
        #     result += (20 - line_up.index(min(line_up)))
        