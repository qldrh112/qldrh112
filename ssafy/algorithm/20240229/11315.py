def f(arr):
    check = False
    for col in range(N):
        for row in range(N):
            if arr[col][row] == 'o':
                for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1]]:
                    for k in range(1, 5):
                        if col + di * k < N and row + dj * k < N and arr[col + di * k][row + dj * k] == 'o':
                            check = True
                        else:
                            check = False
                            break       # for k in range()
                    if check:
                        return 'YES'
    return 'NO'


T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [input() for _ in range(N)]
    print(f'#{t+1} {f(input_arr)}')