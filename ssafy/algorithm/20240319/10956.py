from collections import deque


def min_change(cur):
    global min_v, change
    if cur == N:
        min_v = min(min_v, change)
        return
    else:
        for i in range(1, input_nums[cur]+1):
            change += 1
            if min_v > change:
                min_change(cur+i)
            change -= 1


T = int(input())
for t in range(T):
    input_nums = deque(list(map(int, input().split())))
    N = input_nums.popleft() - 1
    # 시작할 때는 교체 횟수에 포함하지 않으므로
    change, min_v = -1, float('inf')
    min_change(0)
    print(f'#{t+1}', min_v)


