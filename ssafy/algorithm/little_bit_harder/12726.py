def toggle(n, m, arr):
    """
    N: 토글의 크기(n * n)
    M: 초(int)
    arr: 토글의 요소(2차원 리스트)
    return: m초 뒤 arr 에 있는 1의 양
    cnt: 전체 전환하는 횟수
    """
    cnt = 0
    for k in range(1, m+1):
        # m이 k의 배수
        if m % k == 0:
            cnt += 1

        else:
            # 배열 인덱스가 1부터 시작함
            for i in range(N):
                for j in range(N):
                    # 인덱스의 합이 k와 같거나 k의 배수가 되는 영역은 토글
                    if ((i+1) + (j+1)) % k == 0 or ((i+1) + (j+1)) == k:
                        arr[i][j] = abs(arr[i][j]-1)

    num_of_one = 0
    if cnt % 2 == 1:
        for col in range(n):
            if 0 not in arr[col]:
                continue
            for row in range(n):
                if arr[col][row] == 0:
                    num_of_one += 1
    else:
        for col in range(n):
            if 1 not in arr[col]:
                continue
            for row in range(n):
                if arr[col][row] == 1:
                    num_of_one += 1

    return num_of_one


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1} {toggle(N, M, input_arr)}')