N=int(input())

#1+(6*1)+(6*2)+(6*3)+.....


i=1
t=0
while True:
    i+=(6*t)
    t+=1
    if N<=i:
        break

print(t)