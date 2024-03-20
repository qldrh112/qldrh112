def preorder_circuit(t):
    """
    t: 탐색의 시작(노드, int)
    """
    global value
    if t:
        # 왼쪽으로 쭉쭉 내려가고, 그 아래 무언가 없으면 올라와서 값을 던져준다.
        preorder_circuit(left_c[t])
        tree[t] = value
        value += 1
        preorder_circuit(right_c[t])


T = int(input())
for t in range(T):
    N = int(input())
    """
    root: 트리의 근본(int, idx)
    value: 트리를 순회하면서 넣어줄 값(int)
    tree: 트리(1차원 리스트)
    left_c: 부모 노드의 첫번째 자식(int, idx)
    right_c: 부모 노드의 두번째 자식(int, idx)
    """
    root = 1
    value = 1
    tree = [0] * (N + 1)
    left_c = [0] * (N + 1)
    right_c = [0] * (N + 1)

    # 완전 이진 트리에서 부모 노드는 자식 노드의 N//2이므로
    for n in range(1, N//2+1):
        left_c[n] = 2 * n
        # 같거나 작을 때 조건에 진입하게 해야 함
        if 2 * n + 1 <= N:
            right_c[n] = 2 * n + 1

    preorder_circuit(root)

    print(f'#{t+1} {tree[root]} {tree[N//2]}')
