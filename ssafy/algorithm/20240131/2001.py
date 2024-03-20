# 이전에 작성했던 코드
# TC = int(input())
#
# # TC만큼 반복
# for q in range(TC):
#     whole_lst = []
#     output_lst = []
#     M, N = map(int, input().split())
#     p = M - N + 1
#
#     # 파리판 만들기
#     for _ in range(M):
#         input_lst = [input().split()]
#         whole_lst.extend(input_lst)
#
#     # 좌상단 좌표 때렸을 때 잡히는 파리 수
#
#     for col in range(p):
#         for row in range(p):
#             tmp = 0
#             for i in range(N):
#                 for j in range(N):
#                     tmp += int(whole_lst[col + i][row + j])
#             output_lst.append(tmp)
#
#     # 가장 많이 잡힌 파리 수 뽑아 내기
#     output = max(output_lst)
#     print(f'#{q + 1} {output}')

def big_shot(N, M):
    """
    :param N: 파리판의 크기
    :param M: 파리채의 크기
    :return: 파리채를 휘둘렀을 때 가장 많이 잡힌 파리의 수
    """
    p = N-M+1               # 파리채가 범위를 넘어서지 않게 하는 장치
    output = 0              # 한 번에 가장 많이 잡힌 파리

    # 파리판 만들기
    whole_lst = [list(map(int, input().split())) for _ in range(N)]
    # 좌상단 좌표 때렸을 때 잡히는 파리 수
    for col in range(p):
        for row in range(p):
            tmp = 0
            for i in range(M):
                for j in range(M):
                    tmp += int(whole_lst[col+i][row+j])
            # 가장 많이 잡힌 파리 수 뽑아 내기
            if tmp > output:
                output = tmp

    return output

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    print(f'#{t+1} {big_shot(N, M)}')
