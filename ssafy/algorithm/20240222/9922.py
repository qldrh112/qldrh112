# import sys
# sys.stdin = open('input.txt', 'r')

def dec_to_bin(n):
    """
    n: 0부터 1사이의 소수(float)
    return: 십진수에서 변환한 이진수의 소수점 이하 자리(str, 13자 이상 넘어갈 시 0반환)
    """
    output = ''
    cnt = 0

    while n != 0 and cnt < 13:
        output += str(n * 2)[0]
        n = float('0.' + str(n * 2)[2:])
        cnt += 1

    if cnt >= 13:
        return 'overflow'
    else:
        return output


T = int(input())
for t in range(T):
    N = float(input())
    # 츌력합니다.
    print(f'#{t+1} {dec_to_bin(N)}')