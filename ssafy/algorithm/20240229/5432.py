def f(data):
    steel = 0
    stack = []
    for idx, elem in enumerate(data):
        if elem == '(':
            stack.append((idx, elem))
        # 레이저
        elif elem == ')' and idx == stack[-1][0] + 1:
            stack.pop()
            steel += len(stack)
        # 쇠막대기
        else:
            stack.pop()
            steel += 1

    return steel


T = int(input())
for t in range(T):
    input_data = input()
    print(f'#{t+1} {f(input_data)}')