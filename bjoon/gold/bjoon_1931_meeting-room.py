# 겹치지 않는 시간을 최대한 많이 생성하라
N = int(input())


# 타임라인
timeline = []
for _ in range(N):
    
    # times[0]은 시작시간, times[1]은 끝나는 시간
    start, end = map(int, input().split())
    timeline.append((start, end))

'''
# lambda 매개변수 : 표현식(보통 return 값)
# 여기서 이 x는 앞에 있는 timeline 리스트를 말하는 것
# 특정 기준을 가지고 정렬할 때는 이런식으로 정렬하면 된다.
# key에는 반드시 함수가 와야한다. (len, lambda ...)
# 종료 시간을 기준으로 정렬
# 종료 시간이 같으면 시작 시간을 기준으로 정렬
# 종료 시간이 같은 회의가 여러 개 있을 때, 
# 시작 시간이 빠른 회의를 먼저 선택하면 더 많은 회의를 배치할 가능성이 커져요.
# 최대한 시간을 많이 선택해야하니까
# 일찍 끝나는게 우선이고
# 일찍 끝나는 시간이 똑같으면 시작 시간이 더 빠른 회의를 고름으로써
# 더 유리한 선택을 한다.
'''

timeline.sort(key = lambda x : (x[1], x[0]))
# print(timeline)

count = 0
end_time = 0 # 첫 종료 시간을 0이라고 가정
             # 이러면 for문에서 start와 end가 같이 들어가도 
             # end_time 자체는 하나 전인 상태이기 때문에 
             # 전 상태의 끝나는 시점과 다음 상태의 시작 지점으로 for문을 돌릴 수 있다.

for start, end in timeline:
    
    if start >= end_time: # 겹치지 않는 회의 시작
        count += 1
        end_time = end    # 종료 시간 갱신
        
print(count)