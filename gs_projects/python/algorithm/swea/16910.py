"""
메모리: 59,768 kb
실행시간: 176 ms
"""
def point_in_circle():
    cnt = 0
    for x in range(N+1):
        for y in range(N+1):
            # 원 안에 점이 있으면
            if (x**2 + y**2) <= N**2:
                # 원점
                if x == 0 and y == 0:
                    cnt += 1
                # 축 위의 점이 아님
                elif x > 0 and y > 0:
                    cnt += 4
                # 축 위의 점
                else:
                    cnt += 2
    return cnt


T = int(input())
for t in range(T):
    N = int(input())
    print(f'#{t+1} {point_in_circle()}')