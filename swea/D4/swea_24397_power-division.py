T = int(input())

for test_case in range(T):
    X, Y, Z = map(int, input().split())
    number = 0
    
    number = str(pow(X, Y) // Z)[-3:] # 정수부
    dec = str(pow(X, Y) / Z - pow(X, Y) // Z)[2:5] # 실수부

    print(number)
    print(dec)
    # 슬라이싱  
    # zfill(n) n자리를 만족하지 못하면 n자리까지 0을 채워 넣음. n자리를 만족하면 아무것도 안함
    print(f'{number}.{dec.zfill(3)}') 

# 1 <= X, Y, Z <= 10^9 이므로 직접 계산이 불가능함. 런타임 에러가 나옴