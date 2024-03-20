def find_exit(maze):
    """
    maze: 미로(2차원 배열)
    return: 미로 탈출 가능 여부(1: 가능, 0: 불가능)
    """
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    queue = [(1, 1)]
    visited = [[False] * 16 for _ in range(16)]
    visited[1][1] = True

    while queue:
        col, row = queue.pop()

        for direction in directions:
            di, dj = direction
            # 3을 만나면 탈출
            if maze[col+di][row+dj] == 3:
                return 1
            
            # 갈 곳이 있으면 큐에 추가
            elif maze[col+di][row+dj] == 0 and not visited[col+di][row+dj]:
                queue.append((col+di, row+dj))
                visited[col+di][row+dj] = True

    # 더 이상 갈 곳이 없으면 실패
    return 0


for _ in range(10):
    t = int(input())
    input_arr = [list(map(int, input())) for _ in range(16)]
    print(f'#{t} {find_exit(input_arr)}')