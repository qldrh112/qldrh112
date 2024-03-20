def sum_subset(N, k):
    """
    :param N: 부분 집합의 크기
    :param k: 원하는 부분 집합의 합
    :return: k를 만족하는 부분 집합의 개수
    set = {range(1, 12+1)에서 크기 n의 부분 집합의 원소 합이 k를 만족하는 부분 집합의 개수를 반환하는 함수
    """
    count = 0
    subset_lst = []
    main_set = [x for x in range(1, 12+1)]

    # mainset이 가질 수 있는 모든 부분 집합을 만듭니다.
    for i in range(1<<12):
        tmp = []
        for j in range(12):
            if i&(1<<j):
                tmp.append(main_set[j])

    # 길이가 N인 부분집합만 가져 갑니다.
        if len(tmp) == N:
           subset_lst.append(tmp)

    # 부분 집합의 합이 k인 경우 count를 증가합니다.
    for lst in subset_lst:
        if sum(lst) == k:
            count += 1

    return count

T = int(input())
for t in range(T):
    N, k = map(int, input().split())
    print(f'#{t+1} {sum_subset(N, k)}')