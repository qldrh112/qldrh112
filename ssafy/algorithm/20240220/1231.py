def inorder_traversal(t):
    """
    root: 노드의 시작점
    """
    global output
    # 좌측으로 쭉 내려가다가 더 이상 없으면 돌아와서 문자열 찍고
    if t:
        inorder_traversal(left_c[t])
        output += par[t]
        inorder_traversal(right_c[t])


for t in range(10):
    N = int(input())
    # [노드 번호, 문자열, 자식1번호, 자식2번호]
    input_lst = [input().split() for _ in range(N)]
    
    # 부모 자식 관계 정리
    par = [0] * (N + 1)
    left_c = [0] * (N + 1)
    right_c = [0] * (N + 1)

    for lst in input_lst:
        # [노드 번호, 문자열]
        if len(lst) == 2:
            par[int(lst[0])] = lst[1]
        # [노드 번호, 문자열, 자식1]
        elif len(lst) == 3:
            par[int(lst[0])] = lst[1]
            left_c[int(lst[0])] = int(lst[2])
        # [노드 번호, 문자열, 자식1, 자식2]
        else:
            par[int(lst[0])] = lst[1]
            left_c[int(lst[0])] = int(lst[2])
            right_c[int(lst[0])] = int(lst[3])

    root = 1
    output = ''
    inorder_traversal(root)
    print(f'#{t + 1} {output}')