def ballon_pang(N, M, matrix):
    """
    :param N: 세로길이(col)
    :param M: 가로길이(row)
    :param matrix: 풍선판의 2차원 배열
    :return: 날릴 수 있는 꽂가루 수 중 최대값
    """
    # 왼, 오, 위, 아래
    four_way = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    max_v = 0

    for col in range(N):
        for row in range(M):
            pollen = matrix[col][row]
            num = pollen
            for x in range(4):
                di, dj = four_way[x]            # 0 1

                # 1부터 pollen만큼 순차적으로 di, dj에 곱하여 거리를 늘려나갑니다.
                # pollen을 반복문에 넣어버리면 누적된 pollen에 따라서 계속 반복합니다.
                for k in range(1, num+1):        # range(1, 2)
                    if 0 <= col + (di * k) < N and 0 <= row + (dj * k) < M:
                        pollen += matrix[col+(di*k)][row+(dj*k)]
            if max_v < pollen:
                max_v = pollen

    return max_v

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1} {ballon_pang(N, M, matrix)}')