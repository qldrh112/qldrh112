"""
메모리: 61,456 kb
실행시간: 251 ms
"""
def what_is_hour(now, over):
    return (now + over) % 24


T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    print(f'#{t+1} {what_is_hour(A, B)}')