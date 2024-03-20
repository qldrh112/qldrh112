# import sys
# sys.stdin = open('C:/Users/didie/Documents/gs_repo/ssafy/algorithm/emergency_check_sol/input1.txt', 'r')

def continuos_num(lst):
    """
    lst: 당근의 크기가 담긴 리스트
    return: 가장 많이 연속된 수
    """
    # 연속되는 게 없더라도 1이므로
    max_v = 1
    tmp = 1

    for i in range(N - 1):
        # 다음 당근이 크면
        if lst[i] < lst[i+1]:
            tmp += 1
        # 최고 기록 갱신
        elif max_v < tmp:
            max_v = tmp
            # 남은 당근이 모두 연속되어도 최고 기록을 넘지 않으면 반환
            if max_v >= N - 1 - i:
                return max_v
            tmp = 1
        # 다시 측정
        else:
            tmp = 1
    # 끝에 도달했을 때 검정 필요
    if max_v < tmp:
        max_v = tmp
        
    return max_v

T = int(input())
for t in range(T):
    N = int(input())
    input_lst = list(map(int, input().split()))
    print(f'#{t+1} {continuos_num(input_lst)}')