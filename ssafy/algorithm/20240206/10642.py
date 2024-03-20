def check_palindrome(m, n, arr):
    """
    :param m: 회문 검사를 수행할 길이
    :param n: 문자열 리스트의 크기 (n x n)
    :param arr: 회문 검사를 수행할 문자열 리스트
    :return: 회문 문자열
    """

    # 가로 검사
    # count가 회문의 절반 길이와 같으면
    for col in range(n):
        for row in range(n - m + 1):
            count = 0
            for i in range(m // 2):
                if arr[col][row + i] == arr[col][row + m - 1 - i]:
                    count += 1
            if count == m // 2:
                return arr[col][row:row + m]

    # 세로 검사
    # count가 회문의 절반 길이와 같으면
    for row in range(n):
        for col in range(n - m + 1):
            count = 0
            # 2차원에서 컬럼은 슬라이싱이 어려우니 미리 가운데 지정해놓음
            if m % 2 == 0:
                palindrome = [0] * m
            else:
                palindrome = [0] * (m // 2) + [arr[col + m // 2][row]] + [0] * (m // 2)

            for i in range(m // 2):
                if arr[col + i][row] == arr[col + m - 1 - i][row]:
                    count += 1
                    palindrome[i] = palindrome[-1 - i] = arr[col + i][row]

                if count == m // 2:
                    return palindrome


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    string_matrix = [list(input()) for _ in range(N)]
    print(f'#{t + 1}', ''.join(check_palindrome(M, N, string_matrix)))
