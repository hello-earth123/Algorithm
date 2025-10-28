N = int(input())
line = list(map(int, input().split()))


stack = []
current = 1 # 지금 줘야 하는 번호
possible = True


for person in line:
    # 줄 앞 사람이 현재 번호랑 같으면 바로 간식 받으러
    if person == current:
        current += 1

    else:
        # 만약 지금 줄 순서의 사람이 아니다.
        # 줄에 선 사람을 스택에 넣기 전에 스택에 있는 사람이 지금 줄 순서면 계속 꺼내준다.
        while stack and stack[-1] == current:
            stack.pop()
            current += 1

        # 만약 줄에 선 사람의 번호표가 스택 최상단의 번호표 보다 크면 충돌 -> 절대 순서대로 줄 수 없음
        if stack and stack[-1] < person:
            possible = False
            break # break가 없으면 밑에 stack.append 때문에 스택이 엉망이 될 수 있다.

        # 스택이 비어 있거나, 줄에 선 사람이 지금 줄 순서가 아닌데 스택 최상단 번호보다 작으면(LIFO니까 나중에 들어간 친구가 번호가 작아야함)
        # 그럼 스택에 추가 
        stack.append(person)


# 순서 대로 있던 사람들 간식 다 주고 아닌 사람들 스택 다 만들고난 후에
# 스택에 남은 사람들 처리 (아직 대기이신 분들)
while stack:
    # 스택 최상단에 있는 사람이 지금 현재 순서라면 끄집어내기
    if stack[-1] == current:
        stack.pop()
        current += 1

    # 만약 그런 상태가 아니라면 또 순서대로 줄 수가 없음
    else:
        possible = False
        break

if possible:
    print('Nice')
else:
    print('Sad')