N,M=map(int, input().split())

result1=[]
result2=[]
result3=[]
for i in range(1,10001):
    if N%i==0:
        result1.append(i)
    if M%i==0:
        result2.append(i)
    if i%N==0 and i%M==0:
        result3.append(i)


print(max(set(result1) & set(result2))) #& 연산자는 두 집합의 교집합을 의미한다 set함수 다시 공부하기 (여집합, 합집합 찾아보기)
print(min(result3))


