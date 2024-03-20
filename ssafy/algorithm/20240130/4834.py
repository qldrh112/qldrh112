def find_number_frequency(N, number):
    """
    :param N: 카드 수
    :param number: 카드에 쓰인 숫자
    :return: 가장 많이 나온 카드의 숫자와 그 횟수
    """

    counts = [0] * 10           # 카드가 등장하는 횟수
    max_card_count = 0               # 가장 많이 등장한 카드 숫자 반복 횟수
    max_card_number = 0           # 가장 많이 등장한 카드 숫자

    for _ in range(N):             # 카드 숫자를 리스트로
        counts[number%10] += 1
        number //= 10

    for i in range(len(counts)):
        if max_card_count < counts[i]:
            max_card_number = i
            max_card_count = counts[i]

        elif max_card_count == counts[i]:
            if i > max_card_number:
                max_card_number = i

    return max_card_number, max_card_count

T = int(input())
for t in range(T):
    N = int(input())
    input1 = int(input())
    x, y = find_number_frequency(N, input1)

    print(f'#{t+1} {x} {y}')
