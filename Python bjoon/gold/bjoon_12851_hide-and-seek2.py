from collections import deque
def bfs(start, end):
    queue = deque([start])
    distance = [-1] * 100001
    count = [0] * 100001
    distance[start] = 0 # distance 배열은 그 지점에 도착했을 때의 걸린 누적 시간
    count[start] = 1    # count 배열은 그 지점에 몇 번 도착했는지
    # 단순히 visited배열로만 관리한다면 최단 거리(최단 시간)는 보장하지만 한 번 간 곳은 다시 갈 수 없기 때문에
    # count는 모두 1로만 될 수 밖에 없다.
    # 따라서 distane 배열을 통해 최단 시간과 방문 여부를 관리한다.
    # count 배열로 몇 번 방문했는지 관리한다.
    # 그러면 다시 재방문을 할 수 있게 된다.
    # count[x] = "최단 시간에 x에 도달하는 방법의 수"

    while queue:
        location = queue.popleft()
        
        for next_location in (location + 1, location - 1, 2 * location):
            if 0 <= next_location <= 100000:
                # 처음 방문했을 때 (처음 도착했으니 최단 시간 확정)
                if distance[next_location] == -1:
                    distance[next_location] = distance[location] + 1
                    count[next_location] = count[location]
                    queue.append(next_location)
                # 같은 최단 시간으로 또 방문한 경우 
                elif distance[next_location] == distance[location] + 1:
                    count[next_location] += count[location]
    
    return distance[end], count[end]

N, K = map(int, input().split())
result_time = bfs(N, K)
for i in range(len(result_time)):
    print(result_time[i])