'''
v e : v:정점 개수, e:간선 개수
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, n, g):
    """
    시작정점: s
    노드개수: v
    도착지점: g
    큐
    visited
    시작점 인큐
    시작점 방문 표시
    """
    
    q = []
    visited = [0] * (n+1)
    q.append(s)
    visited[s] = 1
    # 처리 하지 않은 정점 탐색
    while q:

        t = q.pop(0)
        if t == g:
            # 시작 정점이 1부터 시작하므로 간선 단위로 계산할 때는 하나 빼줘야 한다.
            return visited[t] - 1
        for neigh in adjl[t]:
            # 방문하지 않은 곳이라면
            if visited[neigh] == 0:
                q.append(neigh)
                visited[neigh] = visited[t] + 1
    # g까지 경로가 없는 경우
    return 0

T = int(input())
for t in range(T):

    v, e = map(int, input().split())
    # 인접 리스트
    adjl = [[] for _ in range(v+1)]

    for i in range(e):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)

    s, g = map(int, input().split())
    print(f'#{t+1} {bfs(s, v, g)}')