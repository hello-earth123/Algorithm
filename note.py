# max heap 삽입 구현
def enq(n):
    global last
    last += 1   # 마지막 정점 추가(생성)
    heap[last] = n  # 그 정점에 번호 저장

    # 이제 부모랑 자식 비교
    c = last
    p = c // 2 # 완전 이진 트리에서의 부모, 자식 번호 연산(heap은 완전 이진 트리니까)
    # (부모가 있고), (부모 < 자식) 이라면 키 값 교환
    # 부모가 있는지를 앞에 둬야 한다.
    while (p > 0) and (heap[p] < heap[c]):
        heap[p], heap[c] = heap[c], heap[p]
        # 새롭게 올라간 자리를 기준으로 (부모를 새로운 자식으로 두고 그 위에 부모랑 비교)
        # 언제까지? -> while (p > 0) and (heap[p] < heap[c])까지
        c = p
        p = c // 2

# 힙 삭제
def deq():
    global last  
    tmp = heap[1] # 루트 백업 (삭제하고 버리면 안됨)
    heap[1] = heap[last] # 마지막 애를 루트로 보냄
    last -= 1            # 마지막 노드 삭제
    p = 1
    c = p * 2
    while c <= last:     # 자식이 하나라도 있으면
        # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
        if c + 1 <= last and heap[c] < heap[c+1]:
            c += 1       # 비교 대상을 오른쪽 자식으로 정함
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:
            break
    return tmp

heap = [0] * 100
last= 0 

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)

    # 마지막 정접 번호
print(heap)

'''
L -> V -> R
preorder

V -> L -> R
inorder

L -> R -> V
postorder
'''

def inorder(root):
    global idx
    lft = root * 2
    rgt = root * 2 + 1
    if lft <= N:
        inorder(lft)
    idx += 1
    tree[root] = idx
    if rgt <= N:
        inorder(rgt)

T = int(input())
for test_case in range(1, T+1):
    tree = [0] * 1001
    idx = 0
    N = int(input())
    inorder(1)
    print(f'#{test_case} {tree[1]} {tree[N // 2]}')