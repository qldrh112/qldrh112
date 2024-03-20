def max_num(arr):
    for i in range(len(arr), 1, -1):
        for j in range(i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr[-1]


def have_view_house(arr, N):
    """
    :param arr: 각 건물의 높이 리스트
    :return: 조망권이 확보된 세대의 총합
    """
    output = 0
    for i in range(N):              # 0~99 # n=100
        # 범위에 따라서 이웃세대의 리스트가 달라진다.
        # 이거 오류처리로 짧게 끊을 수 있는 방법 없나?

        if i == N-2:
            neighbor = [arr[i-2], arr[i-1], arr[i+1]]
        elif i == N-1:
            neighbor = [arr[i-2], arr[i-1]]
        elif i == 1:
            neighbor = [arr[i+1], arr[i+2], arr[i-1]]
        elif i == 0:
            neighbor = [arr[i+1], arr[i+2]]
        else:
            neighbor = [arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2]]

        # 이웃 세대 중 가장 큰 세대와의 차이만큼 조망권이 확보된다.
        if arr[i] > max_num(neighbor):
            output += arr[i] - max_num(neighbor)

    return output


for t in range(10):
    N = int(input())
    height_lst = list(map(int, input().split()))
    print(f'#{t+1} {have_view_house(height_lst, N)}')
