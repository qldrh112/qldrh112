# import sys
# sys.stdin = open('input.txt', 'r')

def div_area(n, arr):
    """
    n: 2차원 영역의 크기(int)
    arr: 2차원 배열
    return: 각 영역의 합의 최대값과 최소값의 차이가 가장 작은 값(int)
    min_v: 최대값과 최소값의 차이가 가장 작은 것
    v_lst: 영역 별 합 데이터
        0 = 좌상단 합
        1 = 우상단 합
        2 = 좌하단 합
        3 = 우하단 합
    """
    v_lst = [0] * 4
    min_v = 2000

    for col in range(n-1):
        for row in range(n-1):
            # 다음 인덱스 부터
            v_lst[0] = sum([arr[x][y] for x in range(col+1) for y in range(row+1)])
            v_lst[1] = sum([arr[x][y] for x in range(col+1) for y in range(row+1, n)])
            v_lst[2] = sum([arr[x][y] for x in range(col+1, n) for y in range(row+1)])
            v_lst[3] = sum([arr[x][y] for x in range(col+1, n) for y in range(row+1, n)])

            if min_v > max(v_lst) - min(v_lst):
                min_v = max(v_lst) - min(v_lst)

    return min_v


T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1} {div_area(N, input_arr)}')