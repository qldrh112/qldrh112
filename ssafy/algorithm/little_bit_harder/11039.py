# import sys
# sys.stdin = open('input.txt', 'w')

# def search_1_square(n, arr):
#     """
#     n: 배열의 크기(n*n)
#     arr: 0과 1로 이루어진 2차원 배열
#     return: 1로 이루어진 사각형의 최대 넓이
#     """
#     max_v = 0

#     for col in range(n):
#         if max_v > (n-col) * n:
#             break                   # for col
#         elif '1' not in arr[col]:
#             continue
#         else:
#             i = col
#             j = arr[col].index('1')
#             output = [0, 0]
#             # y축
#             while arr[i][j] == '1':
#                 output[0] += 1
#                 i += 1

#             # y축 다시 초기화하기
#             i = col
#             # x축
#             while arr[i][j] == '1':
#                 output[1] += 1
#                 j += 1

#             if max_v < output[0] * output[1]:
#                 max_v = output[0] * output[1]

#     return max_v

def dfs(grid, i, j):
    global square
    square += 1
    grid[i][j] = '0'

    if j < N and grid[i][j + 1] == '1':
        dfs(grid, i, j + 1)
    if i < N and grid[i + 1][j] == '1':
        dfs(grid, i + 1, j)
    return 


T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [input().split() for _ in range(N)]
    output = 0
    for i in range(N):
        if '1' not in input_arr[i]:
            continue
        for j in range(N):
            square = 0
            if input_arr[i][j] == '1':
                dfs(input_arr, i, j)
                output = max(square, output)
    print(f'#{t+1}', output)