N = int(input())


for j in range(N):
    result=0
    t=list(map(int, input().split()))
    
    for i in range(10):
        if t[i]%2!=0:
	        result+=t[i]
         
    print(f"#{j+1} {result}")



