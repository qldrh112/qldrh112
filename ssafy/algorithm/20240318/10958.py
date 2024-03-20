# def quick_sort(lst, pivot, lo, hi):
#     while lo <= hi:
#         if lst[lo]
#         while lst[pivot] >= lst[lo]:
#             lo += 1
#         while lst[pivot] <= lst[hi]:
#             hi -= 1
#
#     lst[pivot], lst[hi] = lst[hi], lst[pivot]
#
#


def quick_sort(lst, lo, hi):
    """
    lst: list[int]
    lo: int
    hi: int
    """
    if lo < hi:
        line = partition(lst, lo, hi)
        quick_sort(lst, lo, line - 1)
        quick_sort(lst, line + 1, hi)


def partition(lst, left, right):
    pivot = lst[left]
    i, j = left, right
    while i <= j:
        # 피봇보다 작을 때까지
        while i <= j and lst[i] <= pivot:
            i += 1
        # 피봇보다 클 때까지
        while i <= j and lst[j] >= pivot:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[left], lst[j] = lst[j], lst[left]
    return j


T = int(input())
for t in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    quick_sort(lst, 0, N-1)
    print(f'#{t+1}', lst[N//2])


# def quicksort(A, left, right):
#     if left < right:
#         s = partition(A, left, right)
#         quicksort(A, left, s - 1)
#         quicksort(A, s + 1, right)
#
#
# def partition(A, left, right):
#     p = A[left]
#     i, j = left, right
#     while i <= j:
#         while i <= j and A[i] <= p:
#             i += 1
#         while i <= j and A[j] >= p:
#             j -= 1
#         if i < j:
#             A[i], A[j] = A[j], A[i]
#
#     A[left], A[j] = A[j], A[left]
#     return j
#
#
# A = [7, 5, 4, 1, 2, 10, 3, 6, 9, 8]
# l = 0
# r = len(A) - 1
# quicksort(A, l, r)
# print(A)