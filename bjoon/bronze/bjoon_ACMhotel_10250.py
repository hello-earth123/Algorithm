#Y는 동 -> 나머지
#X는 호수 -> 몫+1
#N=사람수, H=높이, W=넓이, T=테스트 케이스 반복 횟수

#사람 수 나누기 H를 했을 때

T = int(input()) #테스트 케이스


for i in range(T):
    H, W, N = map(int, input().split())

    if N%H==0:
        Y=H
        X=(N//H)
    else:
        Y=N%H
        X=(N//H)+1






    print(str(Y)+str(X).zfill(2))




