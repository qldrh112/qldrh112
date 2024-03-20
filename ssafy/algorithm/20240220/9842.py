def pre_order(T):
    """
    T: 루트(int)
    """
    global cnt
    # 0이 아니다.
    if T:
        cnt += 1
        # 자식 노드 탐색
        pre_order(c1[T])
        pre_order(c2[T])


T = int(input())
for t in range(T):
    cnt = 0
    E, N = map(int, input().split())
    c1 = [0] * (E + 2)
    c2 = [0] * (E + 2)
    p_c_node = list(map(int, input().split()))
    for e in range(E):
        p, c = p_c_node[2 * e], p_c_node[2 * e + 1]
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c

    pre_order(N)
    # 출력합니다.
    print(f'#{t+1} {cnt}')

