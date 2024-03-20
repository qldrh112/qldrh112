def max_profit(lst):
    profit = 0
    i = N - 1
    j = N - 2

    while j >= 0:
        # 전날 가격이 오늘 가격보다 싸다.
        if lst[i] > lst[j]:
            profit += lst[i] - lst[j]
            j -= 1
        # 전날 가격이 오늘 가격보다 비싸다.
        else:
            i = j
            j -= 1

    return profit

T = int(input())
for t in range(T):
    N = int(input())
    input_lst = list(map(int, input().split()))
    print(f'#{t+1} {max_profit(input_lst)}')