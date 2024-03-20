def gns(n, lst):
    """
    :param n: 언어 리스트의 길이
    :param lst: 행성에서 사용하는 언어 리스트
    :return: 정렬된 언어 리스트
    """
    sorted_lst = [0] * n
    language_dict = {
        'ZRO': 0,
        'ONE': 1,
        'TWO': 2,
        'THR': 3,
        'FOR': 4,
        'FIV': 5,
        'SIX': 6,
        'SVN': 7,
        'EGT': 8,
        'NIN': 9,
    }

    counts = [0] * 10
    for i in range(n):
        counts[language_dict[lst[i]]] += 1
        lst[i] = language_dict[lst[i]]

    for i in range(1, 10):
        counts[i] += counts[i-1]

    for i in range(n-1, -1, -1):
        # 원본 데이터의 누적합 리스트에서 하나 줄이고
        counts[lst[i]] -= 1
        # 정렬된 리스트에 원본 데이터를 누적합 리스트의 위치에 넣는다.
        sorted_lst[counts[lst[i]]] = lst[i]

    # 리스트를 순회하며 language딕셔너리의 value와 일치하는 것은 key로 변경합니다.
    for i in range(n):
        for key, value in language_dict.items():
            if sorted_lst[i] == value:
                sorted_lst[i] = key

    return sorted_lst


T = int(input())
for t in range(T):
    tc, N = input().split()
    N = int(N)
    input_lst = list(input().split())
    # 출력합니다.
    print(tc, *gns(N, input_lst))
