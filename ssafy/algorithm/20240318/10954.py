from collections import deque


def merge_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    else:
        left, right = merge_sort(lst[:n//2]), merge_sort(lst[n//2:])

    return merge(deque(left), deque(right))


def merge(left, right):
    """
    left, right: deque[int]
    """
    global cnt
    sorted_lst = []
    if left[-1] > right[-1]:
        cnt += 1

    while left or right:
        if left[0] > right[0]:
            sorted_lst.append(right.popleft())
            if not right:
                sorted_lst += left
                return sorted_lst
        else:
            sorted_lst.append(left.popleft())
            if not left:
                sorted_lst += right
                return sorted_lst


T = int(input())
for t in range(T):
    N = int(input())
    input_lst = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(input_lst)[N//2]
    print(f'#{t+1}', result, cnt)