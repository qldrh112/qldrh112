def who_the_pay_is(ladder):
    """
    :param ladder: 2차원 배열
    :return: 점심내는 사다리의 위치 ladder[0][???]
    2에서부터 까꾸로 올라가면서 점심 내는 사다리의 row를 반환하는 함수
    list.insert로 0을 맨 앞에 넣어서 인덱스가 밀려서 반환은 -1인 값으로 한다.
    """
    x = 0
    y = 100

    # 행에 2개를 추가했기 때문에
    for row in range(100+2):
        if ladder[99][row] == 2:
            x = row

    # 사다리의 높이가 1보다 크고, 범위가 초과되지 않을 때까지
    while y > 1:
        # 사다리의 좌우에 길이 없는 경우
        if ladder[y-1][x-1] == 0 and ladder[y-1][x+1] == 0:
            y -= 1
            if y == 0:
                return x-1

        # 사다리의 왼쪽으로 길이 나있는 경우
        elif ladder[y-1][x-1] == 1:
            x, y = x-1, y-1
            # 사다리 가로를 탄다.
            while ladder[y][x-1] == 1:
                x -= 1

        # 사다리의 오른쪽으로 길이 나있는 경우
        elif ladder[y-1][x+1] == 1:
            x, y = x+1, y-1
            # 사다리 가로를 탄다.
            while ladder[y][x+1] == 1:
                x += 1

    # y = 1일때 한 번에 검정한다.
    if ladder[y-1][x] == 1:
        return x - 1
    elif ladder[y-1][x-1] == 1:
        return x - 2
    elif ladder[y-1][x+1] == 1:
        return x

# 테스트 케이스 0개
for _ in range(10):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    # out of range 예방을 위한 0추가
    for i in range(100):
        matrix[i].insert(0, 0)
        matrix[i].append(0)
    print(f'#{n} {who_the_pay_is(matrix)}')