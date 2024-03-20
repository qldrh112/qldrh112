def attach_papers(n):
    """
    params n: 직사각형의 가로 길이
    return: 20 x n 의 직사각형을 채우는 모든 경우의 수
    """
    # idx = 가로길이//10
    lst = [0] * (n + 1)

    # 채우지 않음, 20x10 하나만 채움
    lst[0] = lst[1] = 1

    """
    가로가 n * 10인 직사각형을 채우는 방법은 가로가 (n-1) * 10 인 경우와
    세로가 (n-2) * 10인 경우 2가지를 더한다.
    """
    for i in range(2, n+1):
        lst[i] = lst[i-1] + 2 * lst[i-2]

    return lst[-1]

T = int(input())
for t in range(T):
    N = int(input())
    # 출력합니다.
    print(f'#{t+1} {attach_papers(N//10)}')