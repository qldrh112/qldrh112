def check_purple(N):
    """
    :param N: 입력 받는 색칠 개수
    :return: 겹치는 데이터 수
    """
    count = 0
    red_tile = []
    blue_tile = []

    for n in range(N):
        list1 = list(map(int, input().split()))         # [3, 6, 6, 8, 1]

        # 레드 판떼기
        if list1[-1] == 1:
            x = abs(list1[3]-list1[1])+1                # 4
            y = abs(list1[2]-list1[0])+1                # 3

            # 보드판 만들기
            arr = [[0] * x for _ in range(y)]           # 4X3

            # 위치 정보 넣기
            for i in range(y):                          # 0 1 2 3
                for j in range(x):                      # 0 1 2
                    arr[i][j] = str(list1[0]+i) + str(list1[1]+j)

            # 레드 판떼기 다 넣기
            red_tile.append(arr)

        # 블루 판떼기
        else:
            x = abs(list1[2]-list1[0])+1
            y = abs(list1[3]-list1[1])+1

            for i in range(x):
                for j in range(y):
                    blue_tile.append(str(list1[0]+i) + str(list1[1]+j))

    for lst in red_tile:
        for red in lst:
            for blue in blue_tile:
                if blue in red:
                    count += 1

    return count

T = int(input())
for t in range(T):
    N = int(input())
    print(f'#{t+1} {check_purple(N)}')