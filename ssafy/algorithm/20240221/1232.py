# def make_tree(n, arr):
#     tree = [0] * (n + 1)
#     for elem in arr:
#         if len(elem) == 2:
#             tree[int(elem[0])] = int(elem [1])
#         else:
#             tree[int(elem[0])] = elem[1]
#     return tree

# def inorder_cal(i, N):

#     # 이거 안 하면 none값 던져져서 typeerror발생
#     if i > N:
#         return 0
    
#     elif tree[i] == '+':
#         left = inorder_cal(2 * i, N)
#         right = inorder_cal(2 * i + 1, N)
#         tree[i] = left + right 
#         return tree[i]
    
#     elif tree[i] == '-':
#         left = inorder_cal(2 * i, N)
#         right = inorder_cal(2 * i + 1, N)
#         tree[i] = left - right
#         return tree[i]
    
#     elif tree[i] == '*':
#         left = inorder_cal(2 * i, N)
#         right = inorder_cal(2 * i + 1, N)
#         tree[i] = left * right
#         return tree[i]
    
#     elif tree[i] == '/':
#         left = inorder_cal(2 * i, N)
#         right = inorder_cal(2 * i + 1, N)
#         tree[i] = left / right
#         return tree[i] 

#     else:
#         return tree[i]
    

# for t in range(10):
#     N = int(input())
#     input_arr = [list(input().split()) for _ in range(N)]
#     operand = [0] * (N + 1)
#     tree = make_tree(N, input_arr)
#     inorder_cal(1, N)
#     # 출력합니다.
#     print(f'#{t+1} {int(tree[1])}')


def inorder_cal(n, arr):
    """
    n: 노드의 개수
    arr: [트리 인덱스, 연산자, 자식1의 인덱스, 자식2의 인덱스]로 구성된 2차원 리스트 
    return: 중위 계산으로 생성된 트리
    """
    tree = [0] * (n + 1)

    for i in range(n-1, -1, -1):
        
        # 피연산자
        if len(arr[i]) == 2:
            tree[int(arr[i][0])] = int(arr[i][1])

        elif arr[i][1] == '+':
            tree[int(arr[i][0])] = tree[int(arr[i][2])] + tree[int(arr[i][3])]

        elif arr[i][1] == '-':
            tree[int(arr[i][0])] = tree[int(arr[i][2])] - tree[int(arr[i][3])]

        elif arr[i][1] == '*':
            tree[int(arr[i][0])] = tree[int(arr[i][2])] * tree[int(arr[i][3])]

        else:
            tree[int(arr[i][0])] = tree[int(arr[i][2])] / tree[int(arr[i][3])]
    
    return tree

for t in range(10):
    # 입력받는 법 익히기
    N = int(input())
    input_arr = [list(input().split()) for _ in range(N)]
    tree = inorder_cal(N, input_arr)
    # 출력합니다.
    print(f'#{t+1} {int(tree[1])}')