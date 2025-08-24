'''
N개의 정점
M개의 쌍
'''

N = int(input())
for _ in range(N-1):
    start_node, end_node, distance = map(int, input().split())
    
