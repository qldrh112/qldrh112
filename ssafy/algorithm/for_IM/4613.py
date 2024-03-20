def min_coloring(arr):

    def white_check(i):
        checker = 0
        for row in range(0, i+1):
            for color in arr[row]:
                if color != 'W':
                    checker += 1
    
        return checker

    def blue_check(i, j):
        checker = 0
        for row in range(i+1, j+1):
            for color in arr[row]:
                if color != 'B':
                    checker += 1
    
        return checker
    
    def red_check(j):
        checker = 0
        for row in range(j+1, N):
            for color in arr[row]:
                if color != 'R':
                    checker += 1
    
        return checker
    

    result = N * M
    for i in range(0, N-2):
        for j in range(i+1, N-1):
            result = min(result, white_check(i) + blue_check(i, j) + red_check(j))

    return result
            

T = int(input())
for t in range(T):
    # N: row M: col
    N, M = map(int, input().split())
    input_arr = [input() for _ in range(N)]
    print(f'#{t+1} {min_coloring(input_arr)}')