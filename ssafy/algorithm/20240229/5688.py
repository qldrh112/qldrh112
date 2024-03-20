def search_cube_root(num):
    """
    num: 세제곱수
    start: 찾고자 하는 일반 정수
    return: start**3 = num 일 때 start
    없으면 -1 반환
    """
    start = num_scope(num)
    while pow(start, 3) <= num:
        if pow(start, 3) == num:
            return start
        start += 1
    return -1


def num_scope(num):
    """
    num: 세제곱수
    10의 제곱 단위로 세제곱 수의 범위를 찾는 함수
    1 <= num**3 <= 1000 <= num**3 <= 1000000  <= num**3 <= 1000000000 <= ...
    return: 일반수
    """
    cube_map = {
        0: pow(1, 3),
        1: pow(10, 3),
        2: pow(100, 3),
        3: pow(1000, 3),
        4: pow(10000, 3),
        5: pow(100000, 3),
        6: pow(1000000, 3),
    }

    for i in range(6, -1, -1):
        if cube_map[i] <= num:
            return 10 ** i

    return 10 ** 6


T = int(input())
for t in range(T):
    input_num = int(input())
    print(f'#{ t +1} {search_cube_root(input_num)}')
