import math

N = int(input())
a = list(map(int, input().split()))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

count = 0
for num in a:
    if is_prime(num):
        count += 1

print(count)
