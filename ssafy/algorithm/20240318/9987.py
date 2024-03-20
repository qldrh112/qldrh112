# 연속해서 같은 방향을 탐색하면 걸린다.
def binary_search():
    global cnt

    for num in M_lst:
        direction = 'neutral'
        point = 1
        lo, hi = 0, N - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if N_lst[mid] == num:
                cnt += point
                break

            # 왼쪽을 고를 때
            elif N_lst[mid] > num:
                hi = mid - 1
                if direction == 'left':
                    point = 0
                direction = 'left'

            # 오른쪽을 고를 때
            else:
                lo = mid + 1
                if direction == 'right':
                    point = 0
                direction = 'right'
    return


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    N_lst = sorted(list(map(int, input().split())))
    M_lst = list(map(int, input().split()))
    cnt = 0
    binary_search()
    print(f'#{t + 1} {cnt}')
