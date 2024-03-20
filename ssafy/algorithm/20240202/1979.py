def word_puzzle(N, K, matrix):
    """
    :param N: 퍼즐판의 크기
    :param K: 단어의 길이
    :param matrix: 퍼즐(2차원 리스트)
    :return: 퍼즐에 K의 길이를 가진 단어가 들어갈 수 있는 경우의 수
    """
    count = 0

    # 행 검증
    for col in range(N):
        row = 0
        # 0을 만나거나 행이 끝날 때까지 끝나지 않는다.
        while row < N:
            word = 0
            while matrix[col][row] == 1:
                word += 1

                if row < N-1:
                    row += 1
                else:
                    break

            if word == K:
                count += 1

            row += 1

    # 열 검증
    for row in range(N):
        col = 0
        # 0을 만나거나 열이 끝날 때까지 끝나지 않는다.
        while col < N:
            word = 0
            while matrix[col][row] == 1:
                word += 1

                if col < N-1:
                    col += 1
                else:
                    break

            if word == K:
                count += 1

            col += 1

    return count

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1} {word_puzzle(N, K, matrix)}')
