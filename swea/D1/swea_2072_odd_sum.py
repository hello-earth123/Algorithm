T = int(input())

for test_case in range(1,T + 1):
    numbers = list(map(int, input().split()))

    result = 0
    for number in numbers:
        if number % 2 != 0:
            result += number

    print(f'#{test_case} {result}')
