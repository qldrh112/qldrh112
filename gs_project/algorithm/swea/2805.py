"""
메모리: 71,540 kb
실행시간: 191 ms
"""
def crops_harvest(arr):
    """
    arr: list[str]
    """
    result = sum(map(int, arr[N // 2]))
    for row in range(N // 2):
        result += sum(map(int, arr[row][N // 2 - row: N // 2 + row + 1])) \
                  + sum(map(int, arr[-1 - row][N // 2 - row: N // 2 + row + 1]))
    return result


T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [input() for _ in range(N)]
    print(f'#{t+1} {crops_harvest(input_arr)}')
