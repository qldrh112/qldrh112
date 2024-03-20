# import sys
# sys.stdin = open('input.txt', 'r')

def hex_to_bin(n, hex_num):
    """
    n: 16진수의 자리수(int)
    hex_num: 16진수(str)
    return: 16진수를 2진수로 변환을 한 문자열(str)
    """
    hex_bin_dict = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    output = ''

    for i in range(n):
        output += hex_bin_dict.get(hex_num[i])

    return output

T = int(input())
for t in range(T):
    N, hex_num = input().split()
    print(f'#{t+1} {hex_to_bin(int(N), hex_num)}')