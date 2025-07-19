#N=int(input())
X,Y,Z=map(int, input().split())

#if Z==9:
    
    
a=list(str(X**Y//Z))
b=list(str(X**Y%Z))

print(a)
print(b)