def effective_loading_dock(arr):
    """
    arr: 하역장 사용 신청 정보
    return: 얼마나 많은 화물차가 하역장을 사용할 수 있는지
    """
    end = arr[0][1]
    cnt = 1
    i = arr

    while i < N:
        if arr[i][0] >= end:
            cnt += 1
            end = arr[i][1]

    return cnt


T = int(input())
for t in range(T):
    # 하역장 사용 신청 수
    N = int(input())
    # list([작업 시작 시간, 작업 종료 시간])
    # 작업 종료 시간 기준 오름차순으로 정렬, 작업 시간 기준으로도 오름차순 정렬
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    input_arr.sort()
    sorted_arr = sorted(input_arr, key=lambda x: x[1])
    print(f'#{t+1} {effective_loading_dock(sorted_arr)}')