def dfs(level):
    global cnt
    cnt += 1
    if level == N:
        return
    else:
        for i in range(N):
            dfs(level + 1)





T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    dfs(0)
    print(cnt)