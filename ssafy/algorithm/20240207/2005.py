def draw_pascal_triangle(n):
    """
    params n: 파스칼의 삼각형 높이
    return: 파스칼의 삼각형 모양 리스트
    """
    # 파스칼의 삼각형 모양으로 2차원 리스트 만들기
    output = [[1] + [0] * i for i in range(n)]
    
    # 각 col의 인덱스0은 다 채워져 있으니까 1부터 시작
    for col in range(1, n):
        for row in range(1, col+1):
            try:
                output[col][row] = output[col-1][row-1] + output[col-1][row]
            # output[col-1][row]를 참조할 때 에러가 난다는 것은 row가 -1인 것이므로 1을 넣어준다.
            except IndexError:
                output[col][row] = 1
    return output


T = int(input())
for t in range(T):
    N = int(input())
    pascal_triangle = draw_pascal_triangle(N)

    # 출력합니다.
    print(f'#{t + 1}')
    for col in range(N):
        print(*pascal_triangle[col])
