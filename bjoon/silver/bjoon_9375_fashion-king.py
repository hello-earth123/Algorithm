# 공집합은 안됨
# 하나만 입어도 상관 없음
T = int(input())

for test_case in range(1, T+1):
    # 의상 갯수
    numbers = int(input())
    result = 1
    
    # 의상 딕셔너리 생성
    dic = {}
    for _ in range(numbers):
        name, kind = map(str, input().split())
        # 딕셔너리에 키가 있다면 +1 업다면 1로 추가
        if kind in dic:
            dic[kind] += 1
        else:
            dic[kind] = 1
            
    
    for key in dic:
        result = result * (dic[key]+1)
    
    
    print(f'{result - 1}')    