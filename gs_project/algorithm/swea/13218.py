"""
메모리: 62,500 kb
실행시간: 335 ms
"""
def max_num_group(student):
    return student // 3


T = int(input())
for t in range(T):
    input_num = int(input())
    print(f'#{t+1} {max_num_group(input_num)}')