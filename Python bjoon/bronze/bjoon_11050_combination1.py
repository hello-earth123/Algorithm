import math

N,K=map(int, input().split())

print(math.comb(N,K))

#import math를 통해서 해결한거지만 import가 없으면 팩토리얼을 통해서 구현해야한다.