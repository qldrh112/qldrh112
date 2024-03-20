def maze_distance(n, maze):
    """
    n: 미로의 크기(int, n*n)
    maze: 미로(2차원 배열)
    return: 시작부터 도착까지의 거리, 0: 도달 불가
    """
    # 3은 제일 위에 있으므로 위부터 탐색
    direction = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    queue = [[-1, -1] for _ in range(n**2+1)]
    visited = [[-1] * N for _ in range(N)]
    front = rear = 0
    cnt = 0

    # 출발 위치, 도착 위치 찾기
    for col in range(n - 1, -1, -1):
        for row in range(n):
            if maze[col][row] == 2:
                queue[rear] = [col, row]
                visited[col][row] = 0

    while queue[front][0] > -1 and queue[front][1] > -1:

        # 현재 위치 뽑기
        h_col, h_row = queue[front]
        front += 1

        # 상하좌우 탐색
        for direct in direction:
            di, dj = direct

            # 인덱스 에러 방지
            if 0 <= di + h_col < n and 0 <= dj + h_row < n:

                # 손을 뻗었을 때 목표 지점에 닿으면
                if maze[di + h_col][dj + h_row] == 3:
                    return visited[h_col][h_row]

                # 이동할 수 있고, 방문하지 않은 곳이라면
                elif maze[di + h_col][dj + h_row] == 0 and visited[di + h_col][dj + h_row] == -1:
                    cnt += 1
                    rear += 1
                    queue[rear] = [di + h_col, dj + h_row]
                    visited[di + h_col][dj + h_row] = visited[h_col][h_row] + 1
    return 0


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # 출력합니다.
    print(f'#{t + 1} {maze_distance(N, arr)}')
