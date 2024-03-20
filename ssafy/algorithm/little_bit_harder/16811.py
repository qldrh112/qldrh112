def count_wild_boars(arr):
    cnt = 0
    for i in range(10):
        cnt += arr[i].find(2)

    return cnt


def wild_boar_alarm(arr):
    """
    n: 밭의 크기(10 * 10)
    arr: 밭과 멧돼지의 위치 정보(2차원 리스트)
    0: 땅, 1: 밭, 2: 멧돼지
    return: 감지되는 멧돼지의 수(int)
    """
    """
    1. 전체 멧돼지 수 찾기
    2. 경보기가 탐지하지 않는 부위 찾기
    3. 거기에 들어가 있는 멧돼지 찾기
    """
    for i in range(10):
        if 1 not in arr[i]:
            continue
        else:
            row = arr[i].index(1)
            col = i
            width = 0
            height = 0
            while arr[col][row] == 1:
                width += 1
                row += 1
            row -= width + 1
            while arr[col][row] == 1:
                height += 1
                col += 1
            col -= height + 1
            break           # for i in
    
    all_wild_boar = count_wild_boars(arr)

    no_detect  = 0
    for i in range(10):
        for j in range(row + 1, row + width-1):
            if arr[i][j] == 2:
                no_detect += 1
    
    for i in range(col + 1, col + height - 1):
        for j in range(10):
            if arr[i][j] == 2:
                no_detect += 1

    return all_wild_boar - no_detect


T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1} {wild_boar_alarm(input_arr)}')