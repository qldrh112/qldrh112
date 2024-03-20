def simple_prime_factorization(num):
    """
    :param num: 소인수분해할 값
    :return: 2^a x 3^b x 5^c x 7^d x 11^e 에서 a, b, c, d, e의 값
    """
    decimal = [2, 3, 5, 7, 11]
    output = [0] * 5
    
    # decimal의 역순으로 순회함
    for i in range(5-1, 0-1, -1):

        # 각 인수의 지수
        indice = 0

        # 인수로 나눠지거나 숫자가 1보다 크다면, 지수를 하나 추가하고 값을 나눠버림
        while num % decimal[i] == 0 and num > 1:
            indice += 1
            num /= decimal[i]

        # 딱 나눠지지 않으면 지수를 output에 추가함
        output[i] = indice

        # 숫자가 1이 된다면 종료
        if num == 1:
            break

    return output


T = int(input())
for t in range(T):
    N = int(input())
    print(f'#{t+1}', *simple_prime_factorization(N))