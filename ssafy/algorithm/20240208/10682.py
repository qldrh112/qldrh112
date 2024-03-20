def graph_cycle_check(v, start, goal, adjl):
    """
    params v: 노드 개수(int)
    params e: 간선의 수(int)
    params start: 노드 시작(int)
    params goal: 노드 도착(int)
    params adjl: 특정 노드에 인접한 노드 번호(2차원 리스트)
    return: start와 goal의 연결 여부(연결:1, 단절:0)
    """
    # 최근 방문 스택, 방문 여부 리스트
    recent_visited_st = []
    visit_lst = [0] * (v+1)

    # 시작 위치를 현위치로 하고, 방문 기록을 찍습니다.
    position = start
    visit_lst[position] = 1

    while True:
        for w in adjl[position]:
            # 도착지에 도달하면 바로 털기
            if w == goal:
                return 1
            
            # 새로운 노드로 이동
            elif visit_lst[w] == 0:
                recent_visited_st.append(position)
                position = w
                visit_lst[position] = 1
                break               # for w in adjl[posi]

        else:
            if recent_visited_st:
                # 현위치를 최근 방문지로
                position = recent_visited_st.pop()

            else:
                return 0               # while True

T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    start, goal = map(int, input().split())

    # 인접 리스트를 만듭니다.
    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = node[i][0], node[i][1]
        adjl[n1].append(n2)

    # 출력합니다.
    print(f'#{t+1} {graph_cycle_check(V, start, goal, adjl)}')