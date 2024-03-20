def f():
    k = D * F / (A + B)
    return k

T = int(input())
for t in range(T):
    D, A, B, F = map(int, input().split())
    print(f'#{t+1} {f()}')
