def f(arr):
    result = 0
    for i in range(N-1):
        time = 0
        for j in range(i+1, N):
            if arr[i][1] > arr[j][0]:
                time += 1

        if result < time:
            result = time

    return result + 1


T = int(input())
for t in range(T):
    N = int(input())
    input_arr = sorted([sorted(list(map(int, input().split()))) for _ in range(N)])
    print(f'#{t+1} {f(input_arr)}')