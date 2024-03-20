def f(man, make_time, bread, arrive_time):
    num_of_bread = 0
    for i in range(man):
        num_of_bread += bread * (arrive_time[i] // make_time)
        arrive_time[i + 1] -= arrive_time[i] 
        if num_of_bread > 0:
            num_of_bread -= 1
        else:
            return 'Impossible'

    return 'Possible'

T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    input_lst = sorted(list(map(int, input().split()))) + [0]
    print(f'#{t+1} {f(N, M, K, input_lst)}')