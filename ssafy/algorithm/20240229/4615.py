def f(row, col, board):
    """
    params row: 0부터 N-1까지
    params col: 0부터 N-1까지
    params board: 오셀로 보드판(2차원 리스트)
    return: 변경된 보드판
    """
    flip = []
    board[row][col] = color
    for drow, dcol in direction:
        power: int = 1
        while 0 <= row + drow * power < N and 0 <= col + dcol * power < N:
            # 빈칸 만나면
            if board[row + drow * power][col + dcol * power] == 0:
                # while
                break
            # 다른 색상 만나면
            elif board[row + drow * power][col + dcol * power] != color:
                flip.append((row + drow * power, col + dcol * power))
            # 같은 색상 만나면
            else:
                for i, j in flip:
                    board[i][j] = color
                # while
                break
            power += 1

        # 초기화
        flip = []
        power = 1


T = int(input())
for t in range(T):
    # 판 크기, 착수
    N, M = map(int, input().split())
    # 오셀로 보드판
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1
    board[N // 2][N // 2] = 2
    # 8방위
    direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    # 검은 돌, 흰 돌의 개수
    cnt_BK = 0
    cnt_WH = 0

    for _ in range(M):
        col, row, color = map(int, input().split())
        # 보드판의 인덱스는 0부터 시작하므로
        f(row-1, col-1, board)

    # 돌 개수 확인
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt_BK += 1
            elif board[i][j] == 2:
                cnt_WH += 1

    print(f'#{t+1} {cnt_BK} {cnt_WH}')
