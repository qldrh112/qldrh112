def max_row(lst):
    """
    :param lst: 리스트
    :return: 각 행의 부분합 중 가장 큰 값
    리스트의 각 행의 부분합 중 가장 큰 값을 반환
    """
    max_value = 100
    for col in range(100):
        row_sum = 0
        for row in range(100):
            row_sum += lst[col][row]
        if max_value < row_sum:
            max_value = row_sum

    return max_value

def max_col(lst):
    """
    :param lst: 리스트
    :return: 각 행의 부분합 중 가장 큰 값
    리스트의 각 열의 부분합 중 가장 큰 값을 반환
    """
    max_value = 100
    for row in range(100):
        col_sum = 0
        for col in range(100):
            col_sum += lst[col][row]
        if max_value < col_sum:
            max_value = col_sum

    return max_value

def max_diag(lst):
    """
    :param lst: 2차원 리스트
    :return: 대각선의 부분합 중 가장 큰 값
    2차원 리스트의 대각의 부분합 중 가장 큰 값을 반환
    """
    diag1 = 0
    diag2 = 0

    for col in range(100):
        for row in range(100):
            # 좌상 -> 우하
            if col == row:
                diag1 += lst[col][row]
            # 우상 -> 좌하
            if col + row == 9:
                diag2 += lst[col][row]
    if diag1 > diag2:
        return diag1
    else:
        return diag2


for t in range(10):
    whatisthis = int(input())

    # 한 줄의 문자열을 입력받아 2차원 리스트로 만들기
    arr = [list(map(int, input().split())) for i in range(100)]

    # 3개 함수를 통해 반환받은 3개의 값 중 가장 큰 것을 반환
    max_value = 100
    return_lst = [max_row(arr), max_col(arr), max_diag(arr)]


    for value in return_lst:
        if max_value < value:
            max_value = value

    print(f'#{t+1} {max_value}')