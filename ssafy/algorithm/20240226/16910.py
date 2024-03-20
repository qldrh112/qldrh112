# def f(N):
#     if N == 1:
#         return 5
#     else:
#         return f(N-1) + 2 * (N-1) + 1 + 4
#
#
# T = int(input())
# for t in range(T):
#     N = int(input())
#     lst = [0] * (N + 1)
#
#     print(f'#{t+1} {f(N)}')


def get_count(N):
    cnt = 0
    for y in range(-N, N + 1):
        for x in range(-N, N+1):
            ans = x ** 2 + y ** 2
            if ans <= N ** 2:
                cnt += 1
    return cnt