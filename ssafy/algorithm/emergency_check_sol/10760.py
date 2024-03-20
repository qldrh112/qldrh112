# import sys
# sys.stdin = open('input.txt', 'r')

def spaceship_landing_point(arr):
    """
    arr: 땅의 높이를 나타낸 2차원 리스트
    return: 착륙 지점으로 사용할 수 있는 곳의 개수
    테두리의 모든 부분을 검정하지 않는 것이 아니다. 모서리 끝부분만 검정하지 않는 것
    """
    cnt = 0
    for col in range(N):
        for row in range(M):
            if col == 0:
                if row == 0 or row == M - 1:
                    continue
            if col == N - 1:
                if row == 0 or row == M - 1:
                    continue
            tmp = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= col + i < N and 0 <= row + j < M:
                        if arr[col][row] > arr[col+i][row+j]:
                            tmp += 1
            if tmp >= 4:
                cnt += 1   
                        
    return cnt 

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1} {spaceship_landing_point(input_arr)}')