"""
메모리: 60,952kb
실행시간: 162 ms
"""

def pow_palindrome_num(A, B):
    nums = list(range(A, B + 1))
    cnt = 0
    for num in pow_palindrome_nums:
        if num in nums:
            cnt += 1
    return cnt


T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    # 1000이하의 제곱 회문 수
    pow_palindrome_nums = [x ** 2 for x in [1, 2, 3, 11, 22]]
    print(f'#{t+1} {pow_palindrome_num(A, min(B, 484))}')