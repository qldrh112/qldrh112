# def arr_min_v(n, arr):
#     """
#     params n: 배열의 크기(int, n*n)
#     params arr: 숫자(1~9)가 들어 있는 배열(list)
#     return: 배열의 최소 합(int)
#     """

def arr_min_v(p, i, n, arr):
    """
    params p: 본 배열에서 인덱스를 결정하기 위한 0부터 n까지의 수열(list)
    params i: 수열의 시작(int)
    params n: 배열의 크기(int, n*n)
    params arr: 숫자(1~9)가 들어 있는 배열(list)
    return: 수열의 모든 부분집합(list)
    min_v: col이 겹치지 않은 조합 중 최솟값
    """
    global min_v
    # 수열이 결정되면 인덱스 수열을 통해 합계를 계산하고, 최솟값 갱신
    if i == n:
        total = sum([arr[idx][value] for idx, value in enumerate(p)])
        if min_v > total:
            min_v = total
    # 수열 뽑기
    else:
        for j in range(i, n):
            p[i], p[j] = p[j], p[i]
            arr_min_v(p, i+1, n, arr)
            p[i], p[j] = p[j], p[i]
    # global 선언을 했다면 리턴은 필요 없음
    return min_v

T = int(input())
for t in range(T):
    # 3 ~ 10
    N = int(input())
    p = [i for i in range(N)]
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 9 * N
    # 출력합니다.
    print(f'#{t+1} {arr_min_v(p, 0, N, input_arr)}')