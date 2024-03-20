def effective_load(nums_of_containers, nums_of_trucks):
    result = 0
    trucks = [True] * M

    for i in range(nums_of_containers):
        for j in range(nums_of_trucks):
            if not trucks[j]:
                continue
            else:
                # 같아도 싣고 갈 수 있다.
                if truck_lst[j] >= weight_lst[i]:
                    trucks[j] = False
                    result += weight_lst[i]
                    break           # for i in nums_of_trucks

    return result


T = int(input())
for t in range(T):
    # N: 컨테이너 수
    # M: 트럭 수
    N, M = map(int, input().split())
    # 컨테이너의 무게(무거운 순으로 받음)
    weight_lst = sorted(list(map(int, input().split())), reverse=True)
    # 트럭의 적재 용량(이건 가벼운 순으로)
    truck_lst = sorted(list(map(int, input().split())))
    print(f'#{t+1} {effective_load(N, M)}')