def check_baby_gin(numbers):
    """

    :param numbers: 받은 패
    :return: Baby Gin / Lose
    """

    # arr = [0] * 6
    #
    # for i in range(6):
    #     arr[i] = numbers[i] % 10
    #     numbers //= 10

    runn = triplet = k = 0
    arr = [int(numbers[x]) % 10 for x in range(6)]  # 위의 주석 처리와 같습니다.

    # 카드 숫자의 개수 정보를 가지고 있는 리스트를 만듭니다.
    counts = [0] * 12
    for i in arr:
        counts[i] += 1

    while k < 10:
        # triplet 검정
        if counts[k] >= 3:
            counts[k] -= 3
            triplet += 1
            continue

        if counts[k] >= 1 and counts[k+1] >= 1 and counts[k+2] >= 1:
            counts[k] -= 1
            counts[k+1] -= 1
            counts[k+2] -= 1
            runn += 1
            continue
        k += 1

    if triplet + runn == 2:
        return 'Baby Gin'
    else:
        return 'Lose'

T = int(input())
for t in range(T):
    input1 = input()
    print(f'#{t+1} {check_baby_gin(input1)}')