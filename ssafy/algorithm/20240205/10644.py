def most_char(str1, str2):
    """
    :param str1: 탐색 대상 문자열 리스트
    :param str2: 탐색하고자 하는 문자열
    :return: str1에 포함된 글자 중 str2에 가장 많이 들어 있는 문자의 개수
    """
    # str1의 중복을 제거합니다.
    str_set = list(set(str1))
    counts = [0] * len(str_set)

    # str1의 문자열을 하나씩 가져와서 str2의 모든 문자열과 비교하여 같으면 counts의 값을 늘립니다.
    for i in range(len(str_set)):
        for j in range(len(str2)):
            if str_set[i] == str2[j]:
                counts[i] += 1

    return max(counts)



T = int(input())
for t in range(T):
    str1 = list(input())
    str2 = list(input())
    print(f'#{t + 1} {most_char(str1, str2)}')
