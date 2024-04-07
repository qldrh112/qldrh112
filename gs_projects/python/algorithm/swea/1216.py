"""
메모리: 64,360 kb
실행시간: 4,204 ms
"""

def longest_palindrome(arr) -> int:
    def n_word_palindrome(length: int):
        # 행과 열 이동 지점
        for x in range(100):
            for i in range(100 - length + 1):
                # 가로 검정(슬라이스는 마지막 인덱스 떼니까)
                if arr[x][i:i+length] == arr[x][i:i+length][::-1]:
                    return True

                # 세로 검정
                tmp = ''
                for y in range(length):
                    tmp += arr[i + y][x]
                if tmp == tmp[::-1]:
                    return True
                
        return False

    for k in range(100, -1, -1):
        if n_word_palindrome(k):
            return k

    return 1


# 회문을 검사하지 못 하는 경우가 존재함
for _ in range(10):
    t = int(input())
    input_arr = [input() for _ in range(100)]
    print(f'#{t} {longest_palindrome(input_arr)}')