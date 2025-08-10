# 정렬할 배열의 범위를 뒤에서부터 하나씩 줄여 나가면서 범위 내에서 순회중에 앞 번호가 뒷 번호 보다 크면 스왑하는 형식
def bubble_sort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                

# 0번 인덱스 값을  최소값이라 가정한 후 리스트 전체를 순회하면서 더 작은 값이 나오면 그 값과 0번 인덱스를 스왑한다.
# 그 후 순회할 리스트의 범위를 앞에서부터 한 칸씩 땡기면서(0번 인덱스가 스왑을 완료했다면 다음은 1번 인덱스) 순회하며 스왑을 진행한다.        
def selection_sort(a, N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        
        

# 리스트 전체를 순회하며 특정 값이 나올 때 마다 counts라는 배열에 각각 1씩 더한다.
# 그 후 counts 리스트를 누적합으로 만든 후에
# 리스트를 뒤에서부터 순회하며 특정 값이 나오면 그 값에 해당하는 counts 배열에서 1씩 뺀 후에 그 뺀 값을 인덱스로 하여 temp라는 최종 리스트에 넣는다.       
def counting_sort(data, temp, k):
    counts = [0] * (k+1)
    
    for i in range(len(data)):
        counts[data[i]] += 1
        
    for i in range(1, k+1):
        counts[i] += counts[i-1]
        
    for i in range(len(data)-1, -1, -1):
        counts[data[i]] -= 1
        temp[counts[data[i]]] = data[i]