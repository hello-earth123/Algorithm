# 왼쪽 방문 안했으면 왼쪽 이동
# 왼쪽 방문 했거나 왼쪽이 없으면 현재 빌딩 들어감
# 현재 빌딩 들어 갔으면 오른쪽으로 들어감
# 다 방문 했으면 부모 노드로 이동
# 왼 -> V -> 오 (중위 탐색)

# 중위 탐색
def tree_inorder(root):
    global idx
    # 만약 부모 자식의 형태로 입력값이 안주어져 있다면 이런식으로 left와 right를 본인이 나눠줘야한다. (only 완전 이진 탐색에서만 사용 가능)
    lft_child = 2*root
    rgt_child = 2*root + 1

    #  중위 순회는 LVR
    # 1. L 왼쪽 트리가 있다면 왼쪽 트리 먼저 탐색
    if lft_child <= (2**K-1):
        tree_inorder(lft_child)

    # 2. V 현재 노드 방문
    tree[root] = arr[idx]
    idx += 1

    # 3. R 오른쪽 트리가 있다면 오른쪽 트리 탐색
    if rgt_child <= (2**K-1):
        tree_inorder(rgt_child)

###########################################################################
###########################################################################

# K는 깊이(레벨)를 의미한다.
K = int(input())
arr = list(map(int, input().split()))
# 트리 생성
# 깊이가 K일 때 노드의 갯수는 2**K - 1이다. 따라서 (트리 리스트는 노드의 갯수+1만큼 만든다.)
tree = [0] * (2**K)
# 변수 설정
idx = 0
# 함수 호출
tree_inorder(1)
# print(tree)

# 레벨별 출력
start = 1
for level in range(K):
    end = 2**level
    print(*tree[start:start+end])
    start += end