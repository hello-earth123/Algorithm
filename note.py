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