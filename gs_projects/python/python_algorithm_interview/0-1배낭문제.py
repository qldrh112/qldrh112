def f(capability, cargo):
    """
    cargo[i][0]: 부피
    cargo[i][1]: 가치
    """
    pack = []
    for i in range(N+1):
        pack.append([])
        for c in range(capability+1):
            # avoid out of range
            if i == 0 or c == 0:
                pack[i].append(0)
            # 짐보다 가방 용량이 크다면
            elif cargo[i-1][0] <= c:
                pack[i].append(
                    max(cargo[i-1][1] + pack[i-1][c - cargo[i-1][0]], 
                    pack[i-1][c]))
            else:
                pack[i].append(pack[i-1][c])
    return pack[-1][-1]


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1} {f(K, input_arr)}')