remainder = []

for i in range(10):
    N = int(input())
    remainder.append(N%42)
    
print(len(set(remainder)))