# def min_typing(string, small_string):
#     """
#     string: 검색하고자 하는 문자열
#     small_string: 뽑아쓸 수 있는 저장된 문자열
#     return: 최소 타이핑 수
#     """
#     count = 0
#     i = 0
#     j = 0
#
#     while i < len(string):
#         count += 1
#
#         # 저장된 문자열과 만나면 다음 저장된 문자열과 만날 수 있게
#         if string[i] == small_string[j]:
#             j += 1
#             i += 1
#
#             # 저장된 문자열이 모두 일치하면 j 초기화, count 감소
#             if j == len(small_string):
#                 count -= j - 1
#                 j = 0
#
#         # 부분 문자열이 0이면 넘기고, 0보다 크면 줄여가면서 문자열의 i 위치에 있는 원소와 비교합니다.
#         elif j == 0:
#             i += 1
#
#         else:
#             j -= 1
#             count -= 1
#
#
#
#     return count
#
# T = int(input())
# for t in range(T):
#     a, b = input().split()
#     print(f'#{t+1} {min_typing(a, b)}')

#
# T = int(input())
# for t in range(T):
#     a, b = input().split()
#
#     print(f'#{t+1}', len(a.replace(b, 'q')))




T = int(input())
for t in range(T):
    A, B = input().split()
    print(f'#{t+1} {len(A.replace(B, "a"))}')

