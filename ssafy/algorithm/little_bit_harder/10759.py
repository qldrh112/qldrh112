import sys
sys.stdin = open('input.txt', 'r')

def figure_round(arr):
    # output = 0
    # for _ in range(N):
    #     input_num = list(map(int, input().split()))
    #     # 변의 길이 = 큰 점 - 작은 점 + 1
    #     output += sum(list(map(lambda x: x * 2, [input_num[2] - input_num[0] + 1, input_num[3] - input_num[1] + 1])))   
    # return output
    b_col = set([x for i in range(N) if arr[i][-1] == 2 for x in range(arr[i][0], arr[i][2]+1)])
    b_row = set([x for i in range(N) if arr[i][-1] == 2 for x in range(arr[i][1], arr[i][3]+1)])

    r_col = set([x for i in range(N) if arr[i][-1] == 1 for x in range(arr[i][0], arr[i][2]+1)])
    r_row = set([x for i in range(N) if arr[i][-1] == 1 for x in range(arr[i][1], arr[i][3]+1)])


    return 


T = int(input())
for t in range(T):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1} {figure_round(input_arr)}')