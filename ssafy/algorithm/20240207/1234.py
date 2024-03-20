# def password_rule(num_lst):
#     """
#     params N: 숫자열의 길이
#     param numbers: 숫자열 리스트
#     """
#     # 임시 변수 trash_bin과 스택의 맨 위 top으로 지정
#     trash_bin = []
#     top = -1
    
#     while len(num_lst) > 1:
        
#         # 연속된 숫자는 제거
#         if num_lst[top] == num_lst[top-1]:
#             num_lst.pop(top)
#             num_lst.pop(top)
            
#             # trash_bin에 무언가 있으면 num_lst로 이전
#             if len(trash_bin) > 0:
#                 num_lst.append(trash_bin.pop(top))
        
#         # 연속되지 않은 숫자는 trash_bin으로
#         else:
#             trash_bin.append(num_lst.pop(top))
    
#     # num_lst에 남은 거 trash_bin의 가장 뒤로 이동
#     # trash_bin = [4, 3, 2, 1]
#     trash_bin.append(num_lst.pop(-1))
    
#     # trash_bin을 역순으로 돌림
#     # trash_bin = [1, 2, 3, 4]
#     trash_bin = [trash_bin[x] for x in range(len(trash_bin)-1, -1, -1)]
    
#     return trash_bin

def password_rule(n, string):
    global cnt
    cnt += 1
    """
    params N: 숫자열의 길이
    param numbers: 비밀번호(str)
    """
    flag, jump = False, False
    result = ''
    for i in range(0, n-1):
        if not jump and string[i] != string[i+1]:
            result += string[i] + string[i+1]
        else:
            flag = True

    if flag:
        pass
    else:
        return string
    
for t in range(10):
    cnt = 0
    N, numbers = input().split()
    # 출력합니다.
    print(f'#{t+1}', password_rule(int(N), numbers))
    print(cnt)