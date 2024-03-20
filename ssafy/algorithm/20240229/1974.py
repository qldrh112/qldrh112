def row_check(arr):
    """
    result(bool)
    0행부터 9행까지 수도쿠의 조건을 만족하는지 확인하여 result 반환
    """
    result = True
    for row in range(9):
        counts = [0] * 10
        for col in range(9):
            counts[arr[row][col]] += 1
        if counts != [0] + [1] * 9:
            return False
    return result


def col_check(arr):
    """
    result(bool)
    0열부터 9열까지 수도쿠의 조건을 만족하는지 확인하여 result 반환
    """
    result = True
    for col in range(9):
        counts = [0] * 10
        for row in range(9):
            counts[arr[row][col]] += 1
        if counts != [0] + [1] * 9:
            return False
    return result


def box_check(arr):
    """
    result(bool)
    9개의 각 박스가 수도쿠의 조건을 만족하는지 확인
    """
    result = True
    for row, col in [[0, 0], [0, 3], [0, 6],
                     [3, 0], [3, 3], [3, 6],
                     [6, 0], [6, 3], [6, 6]]:
        counts = [0] * 10
        for drow in range(3):
            for dcol in range(3):
                counts[arr[row + drow][col + dcol]] += 1
        if counts != [0] + [1] * 9:
            return False
    return result


T = int(input())
for t in range(T):
    input_arr = [list(map(int, input().split())) for _ in range(9)]
    # 조건 확인 -> 출력
    if row_check(input_arr) and col_check(input_arr) and box_check(input_arr):
        print(f'#{t+1}', 1)
    else:
        print(f'#{t+1}', 0)