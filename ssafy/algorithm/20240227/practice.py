# for a in range(1, 4):
#     for b in range(1, 4):
#         for c in range(1, 4):
#             for d in range(1, 4):
#                 print(str(a) + str(b) + str(c) + str(d))
#
# def f(i, lst):
#     n = len(lst) - 1
#     if promising(i, lst):
#
#
# def promising(i, lst)
#
#
# n = 4
# lst = [0] * (n+1)
# f(0, lst)

import sys

# def KFC(x):
#     print(f'{x}번 발동')
#     KFC(x+1)
#
# KFC(0)
# print('끝, 인마')


# def f(i, n):
#     if i == n + 1:
#         return
#     else:
#         print(n, end=' ')
#         f(n+1, n)
#         print(n, end=' ')
#
#
# f(0, 5)

# def f(i):
#     print(i, end=' ')
#     # 깊이가 충족되면 빠꾸
#     if i == level:
#         return
#
#     else:
#         # 재귀 갈기는 횟수
#         for _ in range(branch):
#             f(i + 1)
#
#
# level = 3
# branch = 2
# f(0)

# """
# 깊이: 3
# 너비: 6
# """
#
#
# def f(i):
#     if i == level:
#         print(*path)
#         return
#     else:
#         for j in range(branch):
#             path.append(j + 1)
#             f(i + 1)
#             path.pop(i)
#
#
# path = []
# level, branch = map(int, input().split())
# f(0)

def f1(i):
    # 중복 순열
    if i == N:
        print(*path)
        return
    else:
        for j in range(6):
            path.append(j+1)
            f1(i + 1)
            path.pop()


def f2(i):
    #순열
    global used
    if i == N:
        print(*path)
        return
    else:
        for j in range(6):
            if used[j]:
                continue
            else:
                used[j] = True
                path.append(j + 1)
                f2(i + 1)
                path.pop()
                used[j] = False

N, Type = map(int, input().split())
path = []
used = [False] * 7
if Type == 1:
    f1(0)
else:
    f2(0)