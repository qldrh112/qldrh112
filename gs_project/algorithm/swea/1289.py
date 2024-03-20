"""
메모리: 58,512 kb
실행시간: 149 ms
"""
def count_of_restoration(bit):
    cur, cnt = 0, 0
    for i in range(len(bit)):
        if int(bit[i]) != cur:
            cnt += 1
            cur = abs(cur - 1)

    return cnt


T = int(input())
for x in range(T):
    input_bit = input()
    print(f'#{x+1} {count_of_restoration(input_bit)}')