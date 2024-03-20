def ballon_pang2(N, M, matrix):
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
            for x in range(4):
                di, dj = four_way[x]
                # out of range
                if 0 <= col + di < N and 0 <= row + dj < M:
                    pollen += matrix[col+di][row+dj]
            if max_v < pollen:
                max_v = pollen

    return max_v

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1} {ballon_pang2(N, M, matrix)}')