# import sys
# sys.stdin = open('input.txt', 'r')

"""
받을 수 있는 가장 큰 금액
가지: 3
깊이: 3
같은 숫자가 많으면 change 검정이 불가능
"""


# def make_permutation(i):
#     if i == len(num):
#         take_big_money()
#     else:
#         for j in range(len(num)):
#             if not used[j]:
#                 permutation.append(num[j])
#                 used[j] = True
#                 make_permutation(i + 1)
#                 permutation.pop()
#                 used[j] = False
#
#
# def take_big_money():
#     global max_v
#     change = M + 1
#     for i in range(len(num)):
#         if permutation[i] != num[i]:
#             change -= 1
#         if not change:
#             tmp = int(''.join(permutation))
#             if max_v < tmp:
#                 max_v = tmp

# def make_permutation(i):
#     if i == len(permutation):
#         take_big_money()
#     else:
#         for j in range(len(num)):
#             permutation[i] = j
#             if promising(i):
#                 make_permutation(i + 1)
#
#
# def promising(i):
#     k = 0
#     flag = True
#     while k < i and flag:
#         if permutation[k] == permutation[i]:
#             flag = False
#         k += 1
#     return flag
#
#
# def take_big_money():
#     global max_v
#     diff = 0
#     for i in range(len(num)):
#         if permutation[i] != i:
#             diff += 1
#     # tmp = int(''.join([num[permutation[x]] for x in range(len(num))]))
#     # print(diff - 1, tmp, permutation)
#     if diff == len(num):
#         if diff - 1 == M or diff - 1 in [M - 2 * m for m in range(M)]:
#             tmp = int(''.join([num[permutation[x]] for x in range(len(num))]))
#             # print(tmp)
#             if max_v < tmp:
#                 max_v = tmp
#     elif diff - 1 == M:
#         tmp = int(''.join([num[permutation[x]] for x in range(len(num))]))
#         # print(tmp)
#         if max_v < tmp:
#             max_v = tmp





#
# def make_comb(n, r, s):
#     if r == 0:
#
#     else:
#         for i in range(s, n - r + 1):
#             comb[r - 1] = i
#             make_comb(n, r - 1, i + 1)
#
# def change_digit(i, comb):
#
#
#
#
# T = int(input())
# for c in range(T):
#     num, M = input().split()
#     M = int(M)
#     max_v = 0
#     comb = [0] * 2
#     make_comb(len(num), 2, 0)
#     # print(f'#{c + 1}', max_v)




def combine(n, k):
    results = []

    def dfs(elements, start, k):
        if k == 0:
            results.append(elements[:])
        
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()
    
    dfs([], 1, k)
    return results

n, k = 4, 2
print(combine(n, k))

