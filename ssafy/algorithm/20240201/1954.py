def draw_snail(N):
    """
    :param N: 달팽이의 등껍질의 가로 길이
    :return: 달팽이 등껍질 모양의 리스트
    달팽이의 크기를 입력받아 달팽이의 모양대로 2차원 리스트를 만드는 함수
    """

    arr = [[0] * N for _ in range(N)]
    up = [-1, 0]
    down = [1, 0]
    left = [0, -1]
    right = [0, 1]

    i = j = 0
    k = 1

    # 제자리 찍기
    arr[i][j] = k
    if k == N ** 2:
        return arr

    while k < N ** 2:

        # 오른쪽으로
        # 인덱스를 초과하지 않고, 오른쪽에 0이 있을 때까지
        while j < (N - 1) and arr[i][j + 1] == 0:
            di, dj = right
            k += 1
            arr[i + di][j + dj] = k
            i, j = i + di, j + dj
            if k == N ** 2:
                break

        # 아래쪽으로
        # 인덱스를 초과하지 않고, 아래에 0이 있을 때까지
        while i < (N - 1) and arr[i + 1][j] == 0:
            di, dj = down
            k += 1
            arr[i + di][j + dj] = k
            i, j = i + di, j + dj
            if k == N ** 2:
                break

        # 왼쪽으로
        # 인덱스를 초과하지 않고, 왼편에 0이 있을 때까지
        while j > 0 and arr[i][j - 1] == 0:
            di, dj = left
            k += 1
            arr[i + di][j + dj] = k
            i, j = i + di, j + dj
            if k == N ** 2:
                break

        #  위쪽으로
        # 인덱스를 초과하지 않고, 아래에 0이 있을 때까지
        while i > 0 and arr[i - 1][j] == 0:
            di, dj = up
            k += 1
            arr[i + di][j + dj] = k
            i, j = i + di, j + dj
            if k == N ** 2:
                break
    return arr


T = int(input())
for t in range(T):
    N = int(input())
    snail = draw_snail(N)

    # 출력합니다.
    print(f'#{t + 1}')
    for col in range(N):
        for row in range(N):
            # 행이 N개만큼 출력되면 줄 바꿉니다.
            if row == (N - 1):
                print(snail[col][row])
            else:
                print(snail[col][row], end=' ')