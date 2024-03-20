def num_of_even(nums):
    """
    nums: 숫자 리스트
    return: 짝수의 개수
    """
    cnt = 0
    for num in nums:
        if num % 2 == 0:
            cnt += 1

    return cnt


T = int(input())
for t in range(T):
    N = int(input())
    input_nums = list(map(int, input().split()))
    print(f'#{t+1} {num_of_even(input_nums)}')