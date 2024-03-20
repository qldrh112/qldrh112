import sys
sys.stdin = open('input.txt', 'r')

"""
일꾼이 이동하는 경우
1. 당근 수집을 위한 이동(당근의 인덱스)
2. 수레가 꽉차서 복귀(당근의 인덱스 * 2)
3. 해당 인덱스의 당근 수집(당근의 인덱스 + 1)
4. 모든 당근 수집 완료 후 복귀(당근의 인덱스)
"""

def workload(n, m, lst):
    """
    n: 당근밭의 길이(int)
    m: 수레의 용량
    lst: 각 구역마다 심긴 당근의 양(1차원 리스트)
    return: 당근 수확에 따른 작업자의 이동량(int)
    """
    work_load = 0
    idx = 0
    cart = 0

    while lst != [0] * n:
        # 수레가 꽉차거나
        if m - cart <= lst[idx]:
            lst[idx] -= m - cart
            work_load += (idx + 1) * 2
            cart = 0
        else:
            cart += lst[idx]
            lst[idx] = 0
            idx += 1
    
    # 마지막 당근 운반은 기록되지 않았으므로
    return work_load + idx * 2


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    input_lst = list(map(int, input().split()))
    print(f'#{t+1} {workload(N, M, input_lst)}')