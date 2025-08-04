T = int(input())

for test_case in range(1, T+1):
    stick_laser = str(input())

    # 열렸을 때 한 번 카운트
    open_count = 0

    # 닫히면 조각이 생기는 시점이므로 result에 카운트
    result = 0


    for i in range(len(stick_laser)):
        if stick_laser[i] == '(':
            open_count += 1
        
        else:
            open_count -= 1

            if stick_laser[i-1] == '(':
                result += open_count

            else:
                result += 1

    print(f'#{test_case} {result}')