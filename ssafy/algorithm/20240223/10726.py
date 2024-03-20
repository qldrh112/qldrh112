def bin_rep(n, m):
    """
    n: 마지막 n개의 비트
    m: 정수(bin)
    return: ON(마지막 n 개의 비트가 모두 1이면), OFF(그렇지 않으면)
    """
    checker = (1 << n) - 1

    # & 연산자는 알아서 이진수로 변환하여 계산
    if m & checker == checker:
        return 'ON'
    else:
        return 'OFF'


TC = int(input())
for t in range(TC):
    N, M = map(int, input().split())
    # 출력합니다.
    print(f'#{t+1} {bin_rep(N, M)}')