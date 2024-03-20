def best_divide(employee):
    global max_v, tmp
    if employee == N:
        max_v = max(max_v, tmp[employee])
        return
    else:
        for i in range(N):
            col[employee] = i
            tmp[employee + 1] = tmp[employee] * (input_arr[employee][i] / 100)
            if max_v < tmp[employee + 1] and promising(employee):
                best_divide(employee + 1)


def promising(i):
    k = 0
    flag = True
    while k < i and flag:
        # 일이 중복되거나 가능성이 0이거나 max_v보다 이미 낮거나
        if col[k] == col[i] or not input_arr[k][col[k]]:
            flag = False
        k += 1

    return flag


T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    col = [-1] * N
    tmp, max_v = [1] + [0] * N, 0
    best_divide(0)
    print(f'#{t + 1}{float(max_v * 100): .6f}')