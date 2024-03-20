def min_product_cost(level):
    global min_v
    if level == N:
        min_v = min(min_v, promising2(level))
        return
    else:
        for i in range(N):
            col[level] = i
            if promising1(level) and promising2(level) < min_v:
                min_product_cost(level+1)
            col[level] = -1


def promising1(i):
    k = 0
    flag = True
    while k < i and flag:
        if col[k] == col[i]:
            flag = False
        k += 1
    return flag


def promising2(level):
    return sum([input_arr[x][col[x]] for x in range(level)])


T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    col = [-1] * N
    min_v = float('inf')
    min_product_cost(0)
    print(f'#{t+1} {min_v}')