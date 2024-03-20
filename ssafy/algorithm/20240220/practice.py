"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""

def pre_order(T):
    if T:
        print(T, end=' ')
        pre_order(left[T])
        pre_order(right[T])

# 1번부터 N 번까지의 정점
N = int(input())
E = N - 1
arr = list(map(int, input().split()))
# 부모를 인덱스로 하는 왼쪽 자식 번호 저장
left = [0] * (N + 1)
# 부모를 인덱스로 하는 오른쪽 자식 번호 저장
right = [0] * (N + 1)
# 자식을 인덱스로 하는 부모 저장
par = [0] * (N + 1)

for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    # 왼쪽 자식 놈이 없으면
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p

# 어떤 노드든 찍고 부모노드로 계속 올라가면 level 0 노드를 만날 수 있다.

c = N
# 부모가 있으면
while par[c] != 0:
    # 부모를 자식으로
    c = par[c]
# 더 이상 부모가 없으면 root 는 그 놈이다.
root = c
pre_order(root)