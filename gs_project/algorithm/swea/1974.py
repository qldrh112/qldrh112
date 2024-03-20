def check_sudoku(arr):
    """
    param arr: 2차원 리스트(스도쿠)
    return: 검증 여부
    """
    # row 검증
    for col in range(9):
        counts = [0] * 10
        for row in range(9):

            # 중간에 소단위 검정도 실시합니다.
            # col과 row가 0, 3, 6일 때만 소단위 검사를 돌립니다.
            if col % 3 == 0 and row % 3 == 0:
                small_count = [0] * 10
                for i in range(3):
                    for j in range(3):
                        small_count[arr[col+i][row+j]] += 1
                if small_count != [0] + [1] * 9:
                    return 0

            counts[arr[col][row]] += 1
        if counts != [0] + [1] * 9:
            return 0

    # col 검증
    for row in range(9):
        counts = [0] * 10
        for col in range(9):
            counts[arr[col][row]] += 1
        if counts != [0] + [1] * 9:
            return 0

    # 소그룹 검증
    # for i in range(0, 7, 3):
    #     for j in range(0, 7, 3):
    #         # 검산하는 리스트 확인 잘할 것
    #         counts = [0] * 10
    #         for col in range(3):
    #             for row in range(3):
    #                 counts[arr[i + col][j + row]] += 1
    #         if counts != [0] + [1] * 9:
    #             return 0
    return 1

T = int(input())
for t in range(T):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{t + 1} {check_sudoku(matrix)}')
