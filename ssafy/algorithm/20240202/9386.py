def continuous_1(N, string):
    """
    :param N: 문자열의 길이
    :param string: 입력받은 문자열
    :return: 1이 연속으로 가장 많이 나온 것
    """
    max_v = 0

    for i in range(N-1):
        count = 0
        j = i
        # 마지막이 1인 경우 잡아내기
        while string[j] == '1':
            count += 1
            if j == N-1:
                break
            else:
                j += 1
        # 방향 확인 필요
        if max_v < count:
            max_v = count

    return max_v

T = int(input())
for t in range(T):
    N = int(input())
    string = input()
    print(f'#{t+1} {continuous_1(N, string)}')