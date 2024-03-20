# fx = '(6+5*(2-8)/2)'
# postfix = ''
# stack = [0] * 100
# top = -1
#
# # 스택 밖에서 우선 순위
# icp = {
#     '(': 3,
#     '*': 2,
#     '/': 2,
#     '+': 1,
#     '-': 1,
# }
# # 스택 안에서 우선 순위
# isp = {
#     '(': 0,
#     '*': 2,
#     '/': 2,
#     '+': 1,
#     '-': 1,
# }
#
# for tk in fx:
#     # 여는 괄호 push, 연산자가 top idx의 원소보다 우선순위가 높으면
#     if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):
#         # push
#         top += 1
#         stack[top] = tk
#     # 연산자이고, top의 원소보다 우선순위가 높지 않으면
#     elif tk in '*/+-' and isp[stack[top]] >= icp[tk]:
#         # top원소보다 우선순위가 낮을 때까지 pop
#         while isp[stack[top]] >= icp[tk]:
#             top -= 1
#             postfix += stack[top+1]
#         # push
#         top += 1
#         stack[top] = tk
#     elif tk == ')':
#         while stack[top] != '(':
#             top -= 1
#             postfix += stack[top+1]
#         # 여는 괄호 pop해서 버림
#         top -= 1
#         stack[top+1]
#     # 피연산자인 경우
#     else:
#         postfix += tk
# print(postfix)


# def f(i, k):
#     if i == k:
#         for j in range(k):
#             if bit[j]:
#                 print(arr[j], end=' ')
#         print()
#     else:
#         for j in range(2):
#             bit[i] = j
#             f(i+1, k)
#
# N = 4
# arr = [1, 2, 3, 4]
# # arr[i]가 부분 집합에 포함되었는지 나타내는 배열
# bit = [0] * N
# # bit[i]에 1 또는 0을 채우고, N개의 원소가 결정되면 부분 집합을 반환
# f(0, N)