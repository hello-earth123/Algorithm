switch_number = int(input())

switch_status = list(map(int, input().split()))

student_number = int(input())


# def toggle(switch_status):
#     return 1 - switch_status

# i는 학생 수에 대한 반복 
# j는 스위치 갯수에 대한 반복 -> j는 스위치 번호를 의미한다. 리스트 안에 들어가면 j+1 해야함
# continue는 반복을 중단하고 j가 다음 인자로 넘어가게 동작한다.
# k는 대칭에서 계속 확장되는 보폭
# number -= 1을 통해서 인덱스 번호와 일치시켜 햇갈림을 방지할 수 있다. 
# 변수 위치에 따른 초기화 조심 특히 변수 안에 변수 있을 때 변수1은 바깥, 변수2는 안에 있으면 변수2만 업데이트 되고 변수1은 그대로임
# print문 뒤에 , end = ' '를 통해 줄바꿈 대신 띄어쓰기로 바꿀 수 있다.
# 몇 자 이상 넘어가면 줄바꿈 -> 길이만큼 나눴을 때 나머지가 0이면 print()하면됨
# print()는 줄바꿈의 의미도 가진다.

for i in range(student_number):
    sex, number = map(int, input().split())
    
    #남

    if sex == 1:
        for j in range(1, len(switch_status)+1):
            if (j % number) == 0:
                if switch_status[j-1] == 0:
                    switch_status[j-1] = 1
                else:
                    switch_status[j-1] = 0
            else:
                continue
    #여       
    else:
        if switch_status[number-1] == 0:
            switch_status[number-1] = 1
        else:
            switch_status[number-1] = 0
        k = 1
        while (number - 1) - k >= 0 and (number -1) + k < len(switch_status) and switch_status[(number - 1) - k] == switch_status[(number -1) + k]:
            if switch_status[(number - 1) - k] == 0:
                switch_status[(number - 1) - k] = 1
                switch_status[(number -1) + k] = 1
            else:
                switch_status[(number - 1) - k] = 0
                switch_status[(number -1) + k] = 0
            k += 1
                                    
for i in range(switch_number):
    print(switch_status[i], end=' ')
    if (i + 1) % 20 == 0:
        print()