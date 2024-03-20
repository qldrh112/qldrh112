# x의 n 제곱 값 구하기
# def f(x, n):
#     if n == 1:
#         return x
#     elif n % 2:
#         y = f(x, (n-1)//2)
#         return y ** 2 * x
#     else:
#         y = f(x, n//2)
#         return y ** 2

# 병합정렬
# from collections import deque
#
# def merge_sort(m):
#     n = len(m)
#     if n == 1:
#         return m
#
#     left, right = m[:n//2], m[n//2:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#
#     return merge(deque(left), deque(right))
#
#
# def merge(left, right):
#     result = []
#     while left or right:
#         if left[0] < right[0]:
#             result.append(left.popleft())
#             if not left:
#                 result += right
#                 return result
#         else:
#             result.append(right.popleft())
#             if not right:
#                 result += left
#                 return result
#
#
# m = [2, 3, 4, 6, 7, 8]
# print(merge_sort(m))

lst = [324, 32, 22114, 16, 48, 93, 422, 21, 316]
# [16, 21, 32, 48, 93, 316, 324, 422, 22114]
lst.sort()

# def binary_search(target):
#     cnt = 0
#     lo, hi = 0, len(lst) - 1
#     # 해당 숫자를 찾으면 종료, 찾을 수 없거나
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         cnt += 1
#         if lst[mid] == target:
#             return mid, cnt
#         elif lst[mid] > target:
#             hi = mid - 1
#         else:
#             lo = mid + 1
#     return '목표를 탐색할 수 없다', cnt

def binary_search(lo, hi):
    # 기저조건(언제까지 재귀가 반복되어야 하는가?)
    if lo > hi:
        return -1
    # 다음 재귀 들어가기 전에 전처리
    else:
        mid = (lo+hi)//2
        if lst[mid] == target:
            return mid

        if lst[mid] > target:
            return binary_search(lo, mid-1)
        else:
            return binary_search(mid+1, hi)

    # 다음 재귀함수 호출(파라미터)
    # 함수 마무리한 뒤 작업


target, lo, hi = 22114, 0, len(lst) - 1
print(binary_search(lo, hi))
# target = 321
# print(binary_search(0, len(lst) - 1))
# target = 16
# print(binary_search(0, len(lst) - 1))