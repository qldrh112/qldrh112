def fly_cut(N, M, matrix):
    """
    :param N: 파리판의 크기
    :param M: 파리채의 크기
    :param matrix: 파리 더미(2차원 리스트)
    :return: 파리채로 파리를 후렸을 때 가장 많이 잡는 경우
    """

    max_v = 1
    for col in range(N-M+1):
        for row in range(N-M+1):
            x = 0
            for i in range(M):
                for j in range(M):
                    x += matrix[col+i][row+j]
            if max_v < x:
                max_v = x
    return max_v

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1} {fly_cut(N, M, matrix)}')
