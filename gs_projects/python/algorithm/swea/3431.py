"""
메모리: 62,768 kb
실행시간: 357 ms
"""
def is_enough_workout(lo, hi, train):
    # 운동 부족
    if lo > train:
        return lo - train
    # 적정 범위
    elif hi >= train:
        return 0
    # 운동 과다
    else:
        return -1


T = int(input())
for t in range(T):
    L, U, X = map(int, input().split())
    print(f'#{t+1} {is_enough_workout(L, U, X)}')