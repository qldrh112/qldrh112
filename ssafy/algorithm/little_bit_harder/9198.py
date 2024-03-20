import sys
sys.stdin = open('input.txt', 'r')

"""
1. 전체 멧돼지 수 찾기
2. 경보기가 탐지하지 않는 부위 찾기
3. 거기에 들어가 있는 멧돼지 찾기
"""

def count_wild_boars(arr):
    cnt = 0
    for i in range(10):
        cnt += arr[i].count(2)

    return cnt


def wild_boar_alarm(arr):
    """
    n: 밭의 크기(10 * 10)
    arr: 밭과 멧돼지의 위치 정보(2차원 리스트)
    0: 땅, 1: 밭, 2: 멧돼지
    return: 감지되는 멧돼지의 수(int)
    """
    # 경보기가 탐지하지 못하는 인덱스 찾기
    for i in range(10):
        if 1 not in arr[i]:
            continue
        else:
            row = arr[i].index(1)
            col = i
            width = row
            height = col
            while arr[col][width+1] == 1:
                width += 1
            while arr[height+1][row] == 1:
                height += 1
            break           # for i in

    # 경보기에 감지되지 않는 멧돼지 찾기
    all_wild_boar = count_wild_boars(arr)
    no_detect  = 0
    for i in range(10):
        for j in range(row+1, width):
            if arr[i][j] == 2:
                no_detect += 1
    
    for i in range(col+1, height):
        for j in range(10):
            if arr[i][j] == 2:
                no_detect += 1

    return (all_wild_boar - no_detect)


T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    # 출력합니다.
    print(f'#{t+1} {wild_boar_alarm(input_arr)}')