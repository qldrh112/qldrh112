# def encoding(key):
#     return key ^ 9999
#
#
# def decoding(key):
#     return key ^ 9999
#
#
#
# input_key = int(input())
# print(f'E {encoding(input_key)}')
# print(f'D {decoding(encoding(input_key))}')

# def left_shift(n):
#     for i in range(n):
#         print(bin(0b1 << i), 0b1 << i)
#
#
# n = int(input())
# left_shift(n)


# def bin_rep(n, m):
#     """
#     n: 비트
#     m: 정수
#     """
#     for i in range(n):
#         # 이렇게 자리수를 조작할 수 있다
#         if not 1 & (M >> i):
#             return 'OFF'
#     return 'ON'
#
#
# TC = int(input())
# for t in range(TC):
#     N, M = map(int, input().split())
#     print(f'#{t+1} {bin_rep(N, M)}')

def flaot_print(n):
    print(f'{n:.2f}')
    print(f'{n:.20f}')
    print(f'{n:e}')


n = float(input())
flaot_print(n)