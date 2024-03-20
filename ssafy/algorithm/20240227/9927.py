"""
1. 사무실
2 ~ N. 관리 구역 번호
"""


# def nqueen(i):
#     if i == N:
#         use_energy(col)
#     else:
#         for j in range(N):
#             col[i] = j
#             if promising(i):
#                 nqueen(i + 1)
#
#
# def promising(i):
#     k = 0
#     flag = True
#     while k < i and flag:
#         if col[i] == col[k]:
#             flag = False
#         k += 1
#     return flag
#
#
# def use_energy(col):
#     global min_v
#     tmp = 0
#     for i in range(N):
#         # 전에 했던 것의 row 를 col 으로 따고, 이번의 값을 row 로
#         tmp += input_arr[col[i - 1]][col[i]]
#     if min_v > tmp:
#         min_v = tmp
#
#
# T = int(input())
# for t in range(T):
#     N = int(input())
#     input_arr = [list(map(int, input().split())) for _ in range(N)]
#     col = [0] * N
#     min_v = 999
#     nqueen(1)
#     print(f'#{t + 1}', min_v)


def f1(i, bat):  # i번째로 방문한 관리구역 결정단계, bat 지나온 경로의 소비량
    global min_v
    if i == N:
        print(bat + e[p[N - 1]][0])
        if min_v > bat + e[p[N - 1]][0]:
            min_v = bat + e[p[N - 1]][0]
    elif min_v <= bat:
        return
    else:
        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                p[i] = j  # arr[j]에 j가 들어있음
                f1(i + 1, bat + e[p[i - 1]][p[i]])
                used[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    min_v = 10000
    # arr = [i for i in range(0, N)]  # 사무실0, 관리구역 1-N-1
    used = [0] * N  # 사무실 제외
    p = [0] * N  # 0에서 N-1번까지인 순열
    p[0] = 0  # 맨 앞자리는 0으로 고정
    used[0] = 1
    f1(1, 0)

    print(f'#{tc} {min_v}')
