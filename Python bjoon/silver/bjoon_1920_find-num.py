import sys
input=sys.stdin.readline

N=int(input())

p=set(input().strip().split())

M=int(input())

q=input().strip().split()

for word in q:
    if word in p:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")        

#for word in q:
    # 첫 번째 루프: word = '7'
    # 두 번째 루프: word = '1'
    # 세 번째 루프: word = '5'

