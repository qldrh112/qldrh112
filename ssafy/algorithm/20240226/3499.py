def two_point_algo(lst):
    a = 0
    b = (N + 1) // 2
    turn = 0

    for o in range(N):
        if not turn:
            print(f'#{t + 1}', lst[a], end=' ')
            a += 1
        elif turn % 2 == 1:
            print(lst[b], end=' ')
            b += 1
        else:
            print(lst[a], end=' ')
            a += 1

        turn += 1


T = int(input())
for t in range(T):
    N = int(input())
    input_lst = input().split()
    two_point_algo(input_lst)
    print()
