# import sys
# sys.stdin = open('input.txt', 'r')

def simple_bin_cipher_code(N, M, arr):
    """
    N: 암호의 길이(int)
    M: 문자열의 행 길이(int)
    arr: 암호의 배열(2차원 리스트)
    return: 암호코드의 해석(int, 올바르지 않으면 0)
    """
    code_dict = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }

    code_lst = []
    col = 0
    while '1' not in arr[col]:
        col += 1

    row = -1
    while arr[col][row] == '0':
        row -= 1

    # 앞부터 뽑아서 할 순 없는 것인가?
    for i in range(8):
        tmp = ''
        for j in range(7):
            tmp += arr[col][row-j]
        code_lst.append(tmp[::-1])
        row -= 7

    # 숫자로 변환합니다.
    for i in range(8):
        code_lst[i] = code_dict.get(code_lst[i])
    
    # 암호 해독
    v1 = sum(list(map(lambda x: x * 3, code_lst[1:8:2])))
    v2 = sum(code_lst[0:7:2])

    # 암호 유효성 확인
    if (v1 + v2) % 10 == 0:
        return sum(code_lst)
    else:
        return 0


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    input_arr = [input() for _ in range(N)]
    # 출력합니다.
    print(f'#{t + 1} {simple_bin_cipher_code(N, M, input_arr)}')