def sum_of_node(i, n):
    """
    i: 노드 번호
    n: 노드의 개수
    return: 잎 노드를 방문했을 때 값이 있으면 반환
    """
    if i > n:
        return 0
    else:
        left = sum_of_node(2 * i, n)
        right = sum_of_node(2 * i + 1, n)
        tree[i] += left + right
        return tree[i]
 
T = int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    # 초기 값 설정
    tree = [0] * (N + 1)
    output = 0
    for _ in range(M):
        tree_idx, value = map(int, input().split())
        tree[tree_idx] = value
    sum_of_node(1, N)
    # 출력합니다.
    print(f'#{t+1} {tree[L]}')