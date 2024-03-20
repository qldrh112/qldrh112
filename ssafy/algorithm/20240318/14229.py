# import sys
# sys.stdin = open('input (2).txt', 'r')

# result = sorted(list(map(int, input().split())))[500000]
# print(result)


# def msort(m):
#     if len(m) == 1:     # 원소가 하나만 남은 경우
#         return m
#     mid = len(m)//2
#     left, right = msort(m[:mid]), msort(m[mid:])
#     return merge(left, right)   # 다시 합친 결과 리턴
#
#
# def merge(left, right):
#     result = [0] * (len(left)+len(right))
#     # i : 왼쪽 배열에서 비교할 위치, j : 오른쪽 배열에서 비교할 위치
#     i = j = 0
#     while i < len(left) and j < len(right):  # 양쪽에 비교할 원소가 있는 경우
#         if left[i] < right[j]:
#             result[i+j] = left[i]
#             i += 1
#         else:
#             result[i+j] = right[j]
#             j += 1
#
#     # left의 원소만 남은 경우
#     while i < len(left):
#         result[i+j] = left[i]
#         i += 1
#     while j < len(right):
#         result[i+j] = right[j]
#         j += 1
#     return result
#
# import sys
# sys.stdin = open('100.txt', 'r')
# #arr = [69, 10, 30, 2, 16, 8, 31, 22]
# arr = list(map(int, input().split()))
# arr = msort(arr)
# print(arr[500000])

# 배열을 추가로 만들지 않고  인덱스만 사용하는 방법
def merge(l, mid, r):
    left = l  # 왼쪽 구간의 비교위치, l왼쪽 구간의 첫 원소 인덱스
    right = mid + 1  # 오른쪽 구간의 비교위치, mid+1오른쪽 구간의 첫 원소 인덱스
    tidx = 0
    while left <= mid or right <= r:  # 아직 남은 원소가 있으면
        if left <= mid and right <= r:
            if arr[left] > arr[right]:
                tmp[tidx] = arr[right]
                right += 1
            else:
                tmp[tidx] = arr[left]
                left += 1
        elif left <= mid:  # 왼쪽 구간의 원소만 남아있는 경우
            tmp[tidx] = arr[left]
            left += 1
        else:  # 오른쪽 구간의 원소만 남아있는 경우
            tmp[tidx] = arr[right]
            right += 1
        tidx += 1

    print('이전', arr)
    for i in range(tidx):
        arr[l + i] = tmp[i]
    print('수행', arr)

def merge_sort(l, r):  # l은 정렬 범위 시작 , r 정렬 범위 끝
    if l == r:  # 원소가 1개인경우
        return
    mid = (l + r) // 2
    merge_sort(l, mid)
    merge_sort(mid + 1, r)
    merge(l, mid, r)


arr = [69, 10, 30, 2, 16, 8, 31, 22]
tmp = [0] * len(arr)
merge_sort(0, len(arr) - 1)
print(arr)




def m_sort(left, right):
    if left == right:
        return
    else:
        mid = (left + right) // 2
        m_sort(left, mid)
        m_sort(mid+1, right)
        merge(left, mid, right)

def merge(l, mid, r):
    left = l
    right = mid + 1
    tidx = 0
    # 전체가 tmp에 뿌려져 있지 않으면
    while left <= mid or right <= r:
        # 둘 다 살아 있을 때
        if left <= mid and right <= r:
            # 왼 > 오
            if arr[left] > arr[right]:
                tmp[tidx] = arr[right]
                right += 1
            # 왼 <= 오:
            else:
                tmp[tidx] = arr[left]
                left += 1
        # 하나만 살아있을 때
        elif left <= mid:
            tmp[tidx] = arr[left]
            left += 1

        else:
            tmp[tidx] = arr[right]
            right += 1
        tidx += 1
    for i in range(tidx):
        arr[l+i] = tmp[i]


arr = [69, 10, 30, 2, 16, 8, 31, 22]
tmp = [0] * len(arr)
merge_sort(0, len(arr) - 1)
print(arr)