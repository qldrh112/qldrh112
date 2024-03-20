from pprint import pprint
def find_0(arr, col, row, n):
    """
    params arr: 미로
    params col: 열
    params row: 행
    params n: 배열 한 변의 길이
    return: 0의 위치 정보가 들어있는 리스트(idx: 방향, 0: 왼, 1: 오, 2: 위, 3: 아래)
    """
    crossroads = [0] * 4

    # 왼쪽
    if 0 <= row - 1 and arr[col][row - 1] != 1:
        crossroads[0] = 1
    # 오른쪽
    if row + 1 < n and arr[col][row + 1] != 1:
        crossroads[1] = 1
    # 위쪽
    if 0 <= col - 1 and arr[col - 1][row] != 1:
        crossroads[2] = 1
    # 아래쪽
    if col + 1 < n and arr[col + 1][row] != 1:
        print(arr[col+1][row])
        crossroads[3] = 1
    elif col + 1 < n and arr[col + 1][row] == 1:
        print(arr[col+1][row])
        
    return crossroads

def exit_maze(n, maze):
    """
    params N: 미로 한 변의 길이(N * N)
    params maze: 미로 2차원 배열(0: 이동 가능, 1: 이동 불가, 2: 입구, 3: 출구)
    return: 탈출 가능 여부(0: 불가능, 1: 가능)
    """
    savepoint_stack = []
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

    # 출발점 찾기
    for col in range(n):
        for row in range(n):
            if maze[col][row] == 2:
                savepoint_stack.append([col, row])

    # 시작 지점
    col = savepoint_stack[-1][0]
    row = savepoint_stack[-1][1]

    while True:
        crossroads = find_0(maze, col, row, n)
        print(crossroads)
        # 주변에 0이 없을 때까지
        while 1 in crossroads:
            # 세이브 포인트 저장
            crossroads = find_0(maze, col, row, n)
            count = 0
            for j in range(4):
                if crossroads[j] == 1:
                    count += 1
                    if count == 2:
                        savepoint_stack.append([col, row])
                break  # for j in range(4)

            # 4 방향 갈림길 확인
            for i in range(4):
                if crossroads[i] == 1:
                    maze[col][row] = 1
                    pprint(maze)
                    di, dj = directions[i]
                    col += di
                    row += dj
                    if maze[col][row] == 3:
                        return 1
                    break   # for i in range(4)

        try:
            col, row = savepoint_stack.pop()
        except IndexError:
            return 0
        print(col, row)

T = int(input())
for t in range(T):
    N = int(input())
    input_matrix = [list(map(int, input())) for _ in range(N)]
    print(f'#{t + 1} {exit_maze(N, input_matrix)}')
