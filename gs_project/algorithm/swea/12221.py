"""
메모리: 58,248 kb
실행시간: 148 ms
"""
def calc_mul(a, b):
    return a * b


TC = int(input())
for t in range(TC):
    A, B = map(int, input().split())
    if A > 9 or B > 9:
        print(f'#{t+1}', -1)
    else:
        print(f'#{t+1} {calc_mul(A, B)}')