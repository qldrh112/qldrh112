def array_rotaition(N, arr):
    """
    :param N: 행렬 한 변의 길이
    :param arr: 2차원 리스트
    :return: 90도, 180도, 270도만큼 회전된 2차원 리스트
    """
    output = [[0] * N for _ in range(N)]

    # output 중 1번째 파트
    for row in range(N):
        for col in range(N):
            output[row][N-1-col] = arr[col][row]

    return output

T = int(input())
for t in range(T):
    N = int(input())
    input_lst = [list(map(int, input().split())) for _ in range(N)]
    arr90 = array_rotaition(N, input_lst)
    arr180 = array_rotaition(N, arr90)
    arr270 = array_rotaition(N, arr180)
    # 출력합니다.
    print(f'#{t+1}')
    for i in range(N):
        for j in range(N):
            print(arr90[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr180[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr270[i][j], end='')
        print()

