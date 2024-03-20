def f(i, k, s, t):                  # 0 10 0 10
    global cnt
    cnt += 1

    # 모든 원소가 결정되었을 때
    if s == k:
        print(bit)
        # 부분집합 원소의 합
        for j in range(k):
            # a[j]가 포함된 경우
            if bit[j]:
                print(a[j], end=' ')
        print()

    # 끝까지 도달했음에도 다 찾지 못한 경우
    elif i == k:
        return
    # 고려한 원소의 합이 t보다 큰 경우
    elif s > t:
        return

    else:
        bit[i] = 1
        f(i+1, k, s+a[i], t)
        bit[i] = 0
        f(i+1, k, s, t)
        # for j in range(1, -1, -1):
        #     bit[i] = j
        #     f(i+1, k)

n = 10
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# bit[idx] = a[idx]의 포함 여부
bit = [0] * n
cnt = 0
f(0, n, 0, 10)
print(f'cnt: {cnt}')

# # i = 시작점, k = 순열의 자리수 s= i-1까지 선택한 합
# def f(i, k, s):
#     global cnt
#     cnt += 1
#     global min_v
#     if i == k:
#         # print(*p)
#         # 선택한 원소의 합
#         s = 0
#         for j in range(k):
#             # j행에서 p[j]열을 고른 경우 합 구하기
#             s += arr[j][p[j]]
#         if min_v > s:
#             min_v = s
#         return min_v
#     # 지금 최솟값보다 크다
#     elif s >= min_v:
#         return
#
#     else:
#         # p[i] 위치의 원소 p[j]
#         for j in range(i, k):
#             # p[i] <-> p[j]
#             p[i], p[j] = p[j], p[i]
#             f(i+1, k, s+arr[i][p[i]])
#             # 교환 전으로 복구
#             p[i], p[j] = p[j], p[i]
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# p = [i for i in range(n)]
# min_v = 100
# cnt = 0
# f(0, n, 0)
# print(min_v, cnt)