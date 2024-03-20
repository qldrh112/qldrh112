"""
메모리: 64,344 kb
실행시간: 1193 ms
"""
def calkin_wilf_tree(numerator, denominator, direction):
    """
    numerator: 분자(숫자)
    denominator: 분모(숫자)
    """
    if direction == 'L':
        denominator += numerator
    else:
        numerator += denominator

    return numerator, denominator


T = int(input())
for t in range(T):
    input_string = input()
    numerator, denominator = 1, 1
    for i in range(len(input_string)):
        numerator, denominator = calkin_wilf_tree(numerator, denominator, input_string[i])

    print(f'#{t+1}', numerator, denominator)