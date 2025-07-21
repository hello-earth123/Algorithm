N = int(input())

for _ in range(N):
    X,Y,Z = map(int, input().split())
    val = str(pow(X,Y)/Z)
    int_num,dec_num = map(str, val.split('.'))
    if len(dec_num)>=3:
        print(str(int_num)[-3:] + '.' + (str(dec_num)[:3]))
    elif len(dec_num)<3:
        print(str(int_num)[-3:] + '.' + (str(dec_num).zfill(3)))
    