# def f(arr):
#     cnt = 0
#     standard = arr[-1][1]
#     for i in range(N-1):
#         if standard < arr[i][1]:
#             cnt += 1
#     return cnt

def get_result():
    cnt = 0
    for i in range(N):
        for tar in range(i):
            i_a, i_b = (arr[i][0], arr[i][1])
            tar_a, tar_b = (arr[tar][0], arr[tar][1])
            if i_b < tar_b:
                cnt += 1
    return cnt


T = int(input())
for t in range(T):
    N = int(input())
    arr = []
    for n in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key=lambda x: x[0])
    print(f'#{t + 1} {get_result()}')