def find_path(adjl):
    """
    params n: 정점의 개수 (int)
    params adjl: 특정 노드(인덱스)가 가지는 인접 노드의 번호(2차원 리스트)
    return: 0 -> 99 연결 여부(1: 연결됨, 0: 단절됨)
    """
    visited_lst = [0] * 100
    recent_visited = []
    start = 0
    goal = 99

    position = start
    visited_lst[position] = 1

    while True:
        # 빈 리스트인지 검정해줘야 함
        if adjl[position]:
            for w in adjl[position]:
                if w == goal:
                    return 1
                elif visited_lst[w] == 0:
                    recent_visited.append(position)
                    position = w
                    visited_lst[position] = 1
                    break                       # for w in adjl[position]
            else:
                if recent_visited:
                    position = recent_visited.pop()
                else:
                    return 0
        else:
            position = recent_visited.pop()


for _ in range(10):
    t, N = map(int, input().split())
    node = list(map(int, input().split()))
    adjl = [[] for _ in range(100)]

    for i in range(N):
        n1, n2 = node[i*2], node[i*2+1]
        adjl[n1].append(n2)
    # 출력합니다.
    print(f'#{t} {find_path(adjl)}')