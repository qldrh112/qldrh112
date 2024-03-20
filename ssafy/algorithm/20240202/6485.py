def bus_pass_by(N, bus, busstop, P):
    """
    :param N: 버스 노선의 개수
    :param bus: 버스 노선 리스트
    :param busstop: 버스 정류장 리스트
    :param P: 버스 정류장의 수
    :return: 각 정류장에 몇 개의 버스 노선이 다니는지
    몇 개의 버스가 주어진 버스 정류장을 경유하는지 확인하는 함수
    """
    counts = [0] * (5000 + 1)
    output = [0] * P
    num = 0
    # 버스가 특정 지점을 경유한 경우 해당하는 counts의 인덱스를 1씩 올립니다.
    for point in bus:
        for i in range(point[0], point[1]+1):
            counts[i] += 1

    # 버스 정류장을 하나씩 가져와 그 정류장을 경유한 횟수를 결과에 순서대로 넣습니다.
    for stop in busstop:
        output[num] = counts[stop]
        num += 1

    return output

T = int(input())
for t in range(T):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]              # [[1, 3], [2, 5]]
    P = int(input())
    busstop = [int(input()) for _ in range(P)]          # [1, 2, 3, 4, 5]
    print(f'#{t+1}', *bus_pass_by(N, bus, busstop, P))
