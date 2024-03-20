def N_queen(level):
    global cnt
    if level == N:
        cnt += 1
        return
    else:
        for i in range(N):
            col[level] = i
            if promising(level):
                N_queen(level+1)


def promising(j):
    k = 0
    flag = True
    while k < j and flag:
        # 열이 겹치거나 대각이 겹치면
        if col[k] == col[j] or col[k] + (j-k) == col[j] or col[k] - (j-k) == col[j]:
            flag = False
        k += 1

    return flag


T = int(input())
for t in range(T):
    N = int(input())
    col = [0] * N
    cnt = 0
    N_queen(0)
    print(f'#{t+1}', cnt)