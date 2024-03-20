# def string_comparison(str1, str2):
#     """
#     :param str1: 포함해야 하는 문자열
#     :param str2: 포함되었는지 확인하는 문자열 리스트
#     :return: 1(포함함), 0(포함되지 않음)
#     """

#     count = 0
#     start = 0

#     for i in range(len(str1)):
#         for j in range(start, len(str2)):

#             # str1의 요소가 str2에서 검출되면 count를 1 올리고 반복문 시작 지점을 조정합니다.
#             if str1[i] == str2[j]:
#                 count += 1
#                 start = j + 1
#                 break

#     # str1가 count의 수와 같다면
#     if count == len(str1):
#         return 1
#     else:
#         return 0

def string_comparison(str1, str2):
    if str2.find(str1) == -1:
        return 0
    else:
        return 1

T = int(input())
for t in range(T):
    str1 = input()
    str2 = input()
    print(f'#{t+1} {string_comparison(str1, str2)}')