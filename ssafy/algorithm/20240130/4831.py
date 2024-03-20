def min_charge_num (K, N, M, lst):
    """
    :param K: 한 번 충전으로 이동할 수 있는 거리
    :param N: 종점까지의 거리
    :param M: 충전기가 설치된 수
    :param lst: 충전기가 설치된 곳의 위치 리스트
    :return: 종점으로 가는 최소 충전 수
    """
    for i in range(M-1):                      # (0, 9)
        if lst[i+1] - lst[i] > K:           # 다음 정류소까지 가는 것이 충전량보다 크면
            return 0                        # 0을 반환하는 것 모두 쳐내기
        elif N - lst[-1] > K:
            return 0
        elif lst[0] - 0 > K:
            return 0

    position = 0                               # 현위치
    count = 0                           # 이동 횟수
    while N-K > position:                      # 현위치가 종착지까지 충전 안 해도 될 때까지 반복합니다.
        for j in range(K+position, 0+position, -1):   # 현 위치에서 K칸까지 탐색하여 충전소가 그 안에 있으면 현 위치를 이동합니다.
            if j in lst:
                position = j
                count += 1
                break

    return count





T = int(input())
for t in range(T):
    K, N, M = map(int, input().split())
    input1 = list(map(int, input().split()))                # [1, 3, 5, 7, 9]
    print(f'#{t+1} {min_charge_num(K, N, M, input1)}')
