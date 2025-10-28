H,M=map(int, input().split())

if H==0 and M<45:
    H=23
    M=60-(45-M)
elif H==1 and M<45:
    H=0
    M=60-(45-M)
elif M<45:
    H-=1
    M=60-(45-M)
else:
    H=H
    M=M-45
    
print(H,M)        

    
