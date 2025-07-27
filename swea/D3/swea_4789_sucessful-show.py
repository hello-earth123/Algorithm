T = int(input())


#문자열 인덱스 번호만큼의 사람이이 이상일 때 기립 박수는 하는 사람의 수


for test_case in range(T):

    clap = str(input()) #0~9로 이루어진 '문자열'
    standup_people = 0 # 일어나는 사람 수
    standup_people_need = 0 # 일어나게 하기 위해 필요한 사람 수
    
    for i in range(len(clap)):
        # 만약 기립박수를 하는 사람이 i명 이상일 때 
        # clap[i]만큼 일어난다
        if standup_people >= i:
            standup_people += int(clap[i])
        else:
            standup_people_need += 1
            standup_people += 1+int(clap[i]) # 사람이 모자를 때 필요한 사람을 추가할 때 실제 기립한 사람에도 똑같이 포함시켜줘야 한다
                                             # 그 후 만족을 했을 때의 문자열 clap[i]만큼도 추가로 더해줘야 한다.
                               
    print(f'#{test_case + 1} {standup_people_need}')