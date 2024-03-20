def min_heap(n, lst):
    """
    n: 트리의 크기(int)
    lst: 트리에 넣는 데이터
    return: 최소 힙
    """
    tree = [0] * (n + 1)
    p = 0
    last = 1

    for i in range(n):
        c = last
        p = c // 2
        tree[c] = lst[i]
        while tree[p] != 0 and tree[p] > tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            c = p
            p //= 2
        last += 1

    return tree


def end_to_root(tree):
    """
    tree: 최소 힙
    return: 마지막 노드에서 뿌리까지의 합
    """
    output = 0
    idx = N
    while idx > 1:
        output += tree[idx // 2]
        idx //= 2

    return output


T = int(input())
for t in range(T):
    N = int(input())
    input_lst = list(map(int, input().split()))
    tree = min_heap(N, input_lst)
    # 출력합니다.
    print(f'#{t+1} {end_to_root(tree)}')