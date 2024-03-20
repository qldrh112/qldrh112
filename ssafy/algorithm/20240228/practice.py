# N = 3
# path = []
#
#
# def func(lev, start):
#     if lev == N:
#         print(path)
#         return
#
#     for i in range(start, 7):
#         path.append(i)
#         func(lev+1, i)
#         path.pop()
#
#
# func(0, 1)


# def f():
#     output = 0
#     for i in range(N-1):
#         output += min(lst) * (N - 1)
#
#     return output
#
#
# N = int(input())
# lst = list(map(int, input().split()))
# print(f())


# n = 3
# target = 30
# things = [(5, 50), (10, 60), (20, 140)]
# things.sort(key=lambda x: (x[1]/x[0]), reverse=True)
#
# total = 0
# for kg, price in things:
#     per_price = price / kg
#     if target < kg:
#         total += target * per_price
#         break
#
#     total += price
#     target -= kg
#
# print(int(total))


arr = ['A', 'B', 'C', 'D', 'E']
N = len(arr)
input_min = int(input())
cnt = 0


def get_sub(tar):
    global cnt
    count = 0
    for i in range(N):
        if tar & 0x1:
            count += 1
            if count == 2:
                cnt += 1
                return
        tar >>= 1


for tar in range(0, 1 << N):
    get_sub(tar)

print(cnt)


# n 개 중 2개를 고르는 조합
# N = 4
#
# for i in range(N-1):
#     for j in range(i+1, N):
#         print(i, j)

# def ncr(n, r, s):
#     if r == 0:
#         print(*comb)
#     else:
#         for i in range(s, n - r + 1):
#             comb[r-1] = A[i]
#             ncr(n, r-1, i+1)
#
#
# N = 5
# R = 3
# A = [1, 2, 3, 4, 5]
# comb = [0] * R
# ncr(N, R, 0)

# N = int(input())
# arr = list(map(int, input().split()))
# meeting = []
# for i in range(N):
#     si, fi = arr[i * 2], arr[i * 2 + 1]
#     meeting.append((si, fi))
# # 종료 시간 기준으로 오름차순 정렬
# meeting.sort(key=lambda x: x[1])
# cnt = 0
# fi = 0
# # i 번 회의에 대해
# for i in range(N):
#     # i 번 회의를 선택하려면 si >= fi 현재 진행 중인 회의 이후의 시작
#     if meeting[i][0] >= fi:
#         cnt += 1
#         # 새 회의의 종료 시간
#         fi = meeting[i][1]

# arr = [[2, 2], [1, 3], [1, 2], [3, 1]]
# # [x, y] 좌표 y에 대해 오름차순 정렬, y가 같은 경우 x가 작은 순으로 정렬
# arr.sort()
# # 이것만 하면 두 번째 요구 조건을 만족하지 못함
# arr.sort(key=lambda x: x[1])
# print(arr)