import sys
sys.stdin = open('C:/Users/didie/Documents/gs_repo/ssafy/algorithm/emergency_check_sol/input1.txt', 'r')

"""
1. + 모양 탐색
2. x 모양 탐색
3. 큰 놈 반환
4. 모든 대각 길이를 따는 게 아니라 M으로 범위가 존재함
"""

def sum_col_row(arr):
    """
    arr: 파리의 수가 담긴 2차원 리스트
    return: 가장 많은 파리가 죽는 경우의 파리 양
    """
    max_v = 0
    for col in range(N):
        for row in range(N):
            tmp = arr[col][row]
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                for m in range(1, M):
                    # try로 하면 -인덱스로 뻗어나간다.
                    if 0 <= col + di * m < N and 0 <= row + dj * m < N:
                        tmp += arr[col + di * m][row + dj * m]
                    else:
                        break           # for m
            if max_v < tmp:
                max_v = tmp
    return max_v

def sum_diag(arr):
    """
    arr: 파리의 수가 담긴 2차원 리스트
    return: 가장 많이 파리가 죽는 경우의 파리 수
    """
    max_v = 0
    for col in range(N):
        for row in range(N):
            tmp = arr[col][row]
            for di, dj in [[-1, -1], [1, 1], [1, -1], [-1, 1]]:
                for m in range(1, M):
                    # try로 하면 -인덱스로 뻗어나간다.
                    if 0 <= col + di * m < N and 0 <= row + dj * m < N:
                        tmp += arr[col + di * m][row + dj * m]
                    else:
                        break           # for m
            if max_v < tmp:
                max_v = tmp
    return max_v


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    # 출력합니다.
    print(f'#{t+1} {max([sum_col_row(input_arr), sum_diag(input_arr)])}')