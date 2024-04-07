from collections import defaultdict
n = 10
n1 = 6
edge = [[1, 3], [2, 3], [3, 4], [3, 5], [4, 6], [6, 10], [5, 7], [5, 8], [8, 9]]
edge1 = [[0, 3], [1, 3], [2, 5], [4, 3], [5, 4]]

def find_minheight_tree(n, edges):
    if n <= 1:
        return [0]
    
    # 양방향  그래프 구성
    graph = defaultdict(list)
    for e1, e2 in edges:
        graph[e1].append(e2)
        graph[e2].append(e1)
    print(graph)
    # 첫번째 리프 노드 추가
    leaves = []
    for i in range(n+1):
        if len(graph[i]) == 1:
            leaves.append(i)
    print(graph)
    # 루트 노드만 남을 때까지 반복제거
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)

            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)

        leaves = new_leaves
        print(graph)
    return leaves

print(find_minheight_tree(n1, edge1))