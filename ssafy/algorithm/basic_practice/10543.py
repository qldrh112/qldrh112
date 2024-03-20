def most_min_num(n, nums):
    """
    n: nums 의 개수(int)
    nums: 숫자 리스트
    return: 가장 작은 수의 인덱스
    min_v: 가장 작은 수
    min_idx: 가장 작은 수의 인덱스
    """
    min_idx = -1
    min_v = 1000000000

    for i in range(n):
        if min_v > nums[i]:
            min_idx, min_v = i, nums[i]

    # 몇 번째인지 출력하는 것이므로 1을 더해라
    return min_idx + 1


T = int(input())
for t in range(T):
    N = int(input())
    input_nums = list(map(int, input().split()))
    print(f'#{t+1} {most_min_num(N, input_nums)}')