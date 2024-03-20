def get_carrots(n, carrots):
    """
    n: 당근밭의 길이(int)
    carrots: 인덱스 별 당근의 개수(int)
    return:
    2명의 일꾼이 n번 영역까지 수확할 때의 두 일꾼의 수확의 차이가 최소가 되는지(int),
    이 때 첫번째 일꾼이 수확하는 당근의 개수(int)
    e1: 일꾼1의 당근 수확량
    e2: 일꾼2의 당근 수확량
    min_diff: e1 - e2의 최소가 되는 값
    min_idx: 그 때의 인덱스
    """
    min_diff = 200
    min_idx = -1

    for i in range(2, n):
        e1 = sum(carrots[1:i])
        e2 = sum(carrots[i:])
        if min_diff > abs(e1 - e2):
            min_idx, min_diff = i - 1, abs(e1 - e2)

    return min_idx, min_diff


T = int(input())
for t in range(T):
    N = int(input())
    input_nums = [0] + list(map(int, input().split()))
    print(f'#{t+1}', *get_carrots(N, input_nums))