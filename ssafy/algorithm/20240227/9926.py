# """
# 깊이는 5
# 가지는 2
# """


# def move_arr(i, col, row):
#     """
#     i: path 의 인덱스[int] => (가로 - 2 + 세로)의 길이가 충족되면 값 계산
#     col: 2차원 배열의 열(int)
#     row: 2차원 배열의 행(int)
#     """
#     global min_v
#     if i == 2 * N - 2:
#         if min_v > sum(path):
#             min_v = sum(path)
#     else:
#         for di, dj in [[0, 1], [1, 0]]:
#             if col + di < N and row + dj < N:
#                 path.append(input_arr[col + di][row + dj])
#                 if not used[col+di][row+dj]:
#                     used[col+di][row+dj] = True
#                     move_arr(i + 1, col + di, row + dj)
#                     path.pop()
#                     used[col+di][row+dj] = False


# T = int(input())
# for t in range(T):
#     # 가로 세로 길이(3 <= N <= 13)
#     N = int(input())
#     input_arr = [list(map(int, input().split())) for _ in range(N)]
#     min_v = 130
#     path = [input_arr[0][0]]
#     used = [[False] * N for _ in range(N)]
#     move_arr(0, 0, 0)
#     print(f'#{t+1}', min_v)

from collections import defaultdict
import heapq

T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    graph = defaultdict(list)

    for row in range(N):
        for col in range(N):
            if row + 1 < N:
                graph[row, col].append((input_arr[row+1][col], row+1, col)) 
            if col + 1 < N:
                graph[row, col].append((input_arr[row][col+1], row, col+1))