def min_node_distance(v, s, g):
    '''
    v: 노드의 수(int)
    s: 시작 노드(int)
    g: 목표 노드(int)
    return: s->g 까지의 최소 거리(int)
    '''

    # 큐, visited 만들기
    queue = [-1] * (v + 1)
    visited = [-1] * (v + 1)
    front = rear = -1

    # 시작 노드 꽂기
    rear += 1
    queue[rear] = s
    visited[s] = 0

    # 큐에 뭐가 차있을 때 까지
    while front < v - 1:
        front += 1
        here = queue[front]
        # 목표 노드를 만나면 거리를 반환
        if here == g:
            return visited[here]

        # 현재 위치와 인접한 노드를 탐색하면서 탐색 큐에 추가하고 방문 기록 남김
        for neighbor in adjl[here]:
            if visited[neighbor] == -1:
                rear += 1
                queue[rear] = neighbor
                visited[neighbor] = visited[here] + 1
    return 0


T = int(input())
for t in range(T):
    V, E = map(int, input().split())

    # 인접 노드 만들기
    adjl = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)

    S, G = map(int, input().split())

    # 출력합니다.
    print(f'#{t + 1} {min_node_distance(V, S, G)}')
