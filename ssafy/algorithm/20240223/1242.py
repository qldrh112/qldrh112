import sys
sys.stdin = open('input.txt', 'r')

def cypher_code_scan(n, m, arr):
    """
    n: 배열의 세로크기
    m: 배열의 가로 크기
    arr: 암호코드(2차원 리스트, m * n)
    return: 정상적인 암호코드에 포함된 숫자의 합
    xxxx xxxx 앞 7자리는 상품 고유의 번호 맨 뒷자리는 검증 코드
    (홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드 가 10의 배수
    """
    if N < 100:
        k = 1
    else:
        k = N//100

    code_arr = [
        [3, 2, 1, 1],
        [2, 2, 2, 1],
        [2, 1, 2, 2],
        [1, 4, 1, 1],
        [1, 1, 3, 2],
        [1, 2, 3, 1],
        [1, 1, 1, 4],
        [1, 3, 1, 2],
        [1, 2, 1, 3],
        [3, 1, 1, 2],
        ]

    counts_arr = []
    for q in range(1, k+1):
        counts_arr.extend([list(map(lambda x: x * q, lst)) for lst in code_arr])

    code = []

    for col in range(n):
        if arr[col] == '0' * m:
            continue
        else:
            bin_code = hex_to_bin(m, arr[col])
            start = bin_code.index('1') - 3
            i = start

            while i < len(bin_code) - (7*k):
                j = i + 1
                counts = [0] * 4
                idx = 0

                while idx < 4 and sum(counts) < (7 * k):
                    if idx % 2 == 0:
                        if bin_code[i] == '0':
                            counts[idx] += 1
                            i += 1
                        else:
                            idx += 1
                    else:
                        if bin_code[i] == '1':
                            counts[idx] += 1
                            i += 1
                        else:
                            idx += 1

                # while idx < 4 탈출
                    if 0 not in counts and counts in counts_arr:
                        code.append(counts_arr.index(counts))
                        if len(code) == 8:
                            p1 = sum(list(map(lambda x: x * 3, code[0:8:2])))
                            p2 = sum(code[1:7:2]) + code[-1]
                            if (p1 + p2) % 10 == 0:
                                return sum(code)
                            else:
                                code = []
                                i = j
                else:
                    i = j
    return 0

def hex_to_bin(m, string):
    hex_to_bin_dict = {
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
    bin_code = ''

    for i in range(m):
        if not string[i]:
            bin_code += string[i]
        else:
            bin_code += hex_to_bin_dict.get(string[i])

    return bin_code


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    input_arr = [input() for _ in range(N)]
    print(f'#{t+1} {cypher_code_scan(N, M, input_arr)}')