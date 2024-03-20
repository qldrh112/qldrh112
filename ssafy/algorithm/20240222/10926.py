# import sys
# sys.stdin = open('input.txt', 'r')

def bit_to_dec(str):
    """
    str: 2진수 (7bit * 10개)
    return: 10진수(lst)
    dec: 7자로 끊은 2진수
    output: 10개의 10진수로 이루어진 반환할 리스트
    """
    output = [0] * 10
    for i in range(10):
        dec = 0
        for j in range(7):
            # 문자열로 저장했으므로
            if str[7 * i + j] == '1':
                dec += 2**(6-j)
        output[i] = dec

    return output


T = int(input())
for t in range(T):
    input_data = input()
    print(f'#{t+1}', *bit_to_dec(input_data))