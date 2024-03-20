# # 피보나치 수 dp 적용 알고리즘
# def fibo2(n):
#     f = [0] * (n+1)
#     f[0] = 0
#     f[1] = 1
#     for i in range(2, n+1):
#         f[i] = f[i-1] + f[i-2]
#
#     return f[n]


def dfs(v, n):
    # 시작 v, 마지막 n
    # visited, stack 생성 및 초기화
    visited = [0] * (n + 1)

    # 방문한 놈들
    st = []

    # 방명록 작성
    visited[v] = 1

    # 어디를 방문했는가?
    print(v)

    # 탐색
    while True:
        # 방문한 정점에서 인접하고
        for w in adjl[v]:

            # 방문하지 않은 정점w 가 있으면
            if visited[w] == 0:
                
                # v를 지나서
                st.append(v)

                # w에 방문
                v = w

                # 방명록 작성
                visited[v] = 1
                print(v)

                break  # for w in adjl[j]
        else:
            # v에 남은 인접 정점이 없고
            # 스택이 비어있지 않으면(지나온 정점이 남아 있으면)
            if st:

                # 최근 방문지에서 하나 뽑아서 while 돌려버리기
                v = st.pop()

            # 스택이 비어 있으면(출발점에서 남은 정점이 없으면)
            else:
                break  # while True

    return


"""
v = 정점의 수
e = 연결된 정점의 개수
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

V, E = map(int, input().split())

# 인접 리스트
arr = list(map(int, input().split()))  # [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# ardl[i] 행에 i에 인접인 정점 번호
adjl = [[] for _ in range(V + 1)]
"""
0[[]            
1[2, 3]
2[1, 4, 5]
3[1, 7]
4[2, 6]
5[2, 6]
6[4, 5, 7]
7[6, 3]]
"""
for i in range(E):
    # 연결하기
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    # 방향이 없는 경우
    adjl[n1].append(n2)
    adjl[n2].append(n1)
    # 방향이 있는 경우(1->3)
    # adjl[n1].append(n2)

dfs(1, V)

# def dfs(j, V): # 시작 j, 마지막 V
#     visited[j] = 1            # 방문 표시
#     print(j)                # 출력
#     # j에 인접하고 방문 안 한 w가 있으면
#     for w in adjl[j]:
#         if visited[w] == 0:
#             dfs(w)
#
# # 인접 리스트
# V, E = map(int, input().split())
# arr = list(map(int, input().split()))
#
# adjl = [[] for _ in range(V + 1)]  # ardl[i] 행에 i에 인접인 정점 번호
# visited = [0] * (V+1) # visited, stack 생성 및 초기화
# for i in range(E):
#     # 연결하기
#     n1, n2 = arr[i * 2], arr[i * 2 + 1]
#     adjl[n1].append(n2)
#     adjl[n2].append(n1)  # 방향이 없는 경우
#
# dfs(1, V)
