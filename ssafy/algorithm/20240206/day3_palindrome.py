def x_word_palindrome(x, arr):
    """
    param x: 찾아야 하는 회문의 길이
    param arr: 2차원 문자열 리스트
    return: x글자 회문의 수
    """
    count = 0
    # row 검증
    for col in range(8):
        for row in range(8-x+1):
            if arr[col][row:row+x] == arr[col][row:row+x][::-1]:
                count += 1

    # col 검증
    for row in range(8):
        for col in range(8-x+1):
            # 세로 카운트 위치 주의
            col_count = 0
            for i in range(x//2):
                if arr[col+i][row] == arr[col+x-i-1][row]:
                    col_count += 1
                else:
                    break           # for i in range(x//2)
            if col_count == x//2:
                count += 1

    return count

for t in range(10):
    N = int(input())
    matrix = [input() for _ in range(8)]
    print(f'#{t+1} {x_word_palindrome(N, matrix)}')