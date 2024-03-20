def check_col_magnet(arr):
    """
    arr: 2차원 리스트(list[int][int] = int)
    """
    global cnt
    is_red = False
    for col in range(N):
        # N 극 발견
        if arr[col][row] == 1:
            is_red = True
        # N 극을 이미 발견했으며 S극을 발견했을 때
        elif is_red and arr[col][row] == 2:
            cnt += 1
            is_red = False


for t in range(10):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    # 0행부터 99행까지 열 검사를 수행합니다.
    for row in range(N):
        check_col_magnet(input_arr)
    print(f'#{t+1}', cnt)