import sys
sys.stdin = open('input.txt', 'r')

"""
1. 영역별 당근 수확량 리스트
2. 배열 순회하면서 각 영역별 찾기
3. 배열 돌리는 함수
4. max - min 리턴
"""

def rotation_arr(n, arr):
    """
    n: arr 의 크기(n * n)
    arr: 2차원 리스트
    return: 오른쪽으로 90도 회전한 리스트
    """
    arr90 = [[0] * n for _ in range(n)]
    for col in range(n):
        for row in range(n):
            arr90[row][n-col-1] = arr[col][row]

    return arr90

def get_carrots(n, arr):
    """
    n: arr 의 크기(n * n)
    arr: 2차원 리스트
    return: 영역의 수확량 중 가장 큰 값 - 영역의 수확량 중 가장 작은 값
    """
    carrots_yield = [0] * 4

    for i in range(4):
        if i:
            # arr 를 돌린 arr90 으로 지정해야 함
            arr = rotation_arr(n, arr)
        for col in range(n//2):
            for row in range(n - (2 * (col + 1))):
                # 합을 계속 더해라
                carrots_yield[i] += arr[col][col+1+row]

    return max(carrots_yield) - min(carrots_yield)

T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1} {get_carrots(N, input_arr)}')