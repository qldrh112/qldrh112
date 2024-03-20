# def kmp(t, p):
#     n = len(t)
#     m = len(p)
#     lps = [0] * (m+1)
#     # preprocessing
#     j = 0       # 일치한 개수 == 비교할 패턴 위치
#     lps[0] = -1
#     for i in range(1, m):
#         lps[i] = j          # p[i] 이전에 일치한 개수
#         if p[i] == p[j]:
#             j += 1
#         else:
#             j = 0
#     lps[m] = j
#     # search
#     i = 0           # 비교할 텍스트 위치
#     j = 0           # 비교할 패턴 위치
#     while i < n and j <= m:
#         if j == -1 or t[i] == p[j]:     # 첫글자가 불일치 했거나, 일치하면
#             i += 1
#             j += 1
#         else:                           # 불일치
#             j = lps[j]
#         if j == m:
#             print(i-m, end=' ')
#             j = lps[j]
#     print()
#     return

def expand(left, right):
    while left >= 0 and right <= len(s) and s[left] == s[right-1]:
        left -= 1
        right += 1
    return s[left+1:right-1]


s = 'ki1'

if len(s) < 2 or s == s[::-1]:
    print(s)

result = ''
for i in range(len(s) - 1):
    result = max(result,
                 expand(i, i + 1),
                 expand(i, i + 2),
                 key=len)
print(result)