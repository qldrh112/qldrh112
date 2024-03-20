def max_minus_min(lst):
    return sorted(lst)[-1] - sorted(lst)[0]
    
T = int(input())

for t in range(T):
    N = int(input())
    number_list = list(map(int, input().split()))
    print(f'#{t+1} {max_minus_min(number_list)}')



