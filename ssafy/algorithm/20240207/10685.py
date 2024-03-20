# def delete_duplicate_word(string):
#     """
#     params string: 반복 문자를 지우고자 하는 문자열 리스트
#     return: 남은 문자의 수(int)
#     """

#     trash_bin = []

#     while len(string) > 1:

#         # string의 맨위와 그 아래가 같으면 삭제
#         if string[-1] == string[-2]:
#             string.pop(-1)
#             string.pop(-1)

#             # 쓰레기통의 맨 위에서 가져옵니다.
#             if len(trash_bin) != 0:
#                 string.append(trash_bin.pop(-1))

#         # string의 맨 위와 그 아래가 같지 않으면
#         else:
#             trash_bin.append(string.pop(-1))

#     # string과 쓰레기통에 남은 문자 반환
#     return len(string) + len(trash_bin)

from collections import Counter

def delete_duplicate_word(string):
    """
    params string: 반복 문자를 지우고자 하는 문자열 리스트
    return: 남은 문자의 수(int)
    """

    counter, trash_bin = Counter(string), []

    

    # string과 쓰레기통에 남은 문자 반환
T = int(input())
for t in range(T):
    input_str = input()
    # 출력합니다.
    print(f'#{t+1} {delete_duplicate_word(input_str)}')