def prefix_cal1(n, formula):
    """
    params N: 계산하고자 하는 문자열의 길이 (int)
    params input1: 중위 계산식(str)
    return: 계산결과 (int)
    """
    # 후위 계산식을 담을 스택
    stack = []
    # 계산을 수행하는 스택
    output = []

    # 피연산자와 연산자를 한 번에 처리하므로 n//2+1번 반복
    # ex) “3+4+5+6+7” -> “3, +4, +5, +6, +7”
    for _ in range(n//2+1):
        if len(formula) > 1 and str.isdigit(formula[-1]):
            stack.append(formula.pop(-2))
            stack.append(formula.pop())
        # idx[0]을 위한 코드
        else:
            stack.append(formula.pop())

    for _ in range(n):
        # 피연산자면 담고
        if str.isdigit(stack[-1]):
            output.append(stack.pop())
        # 연산자면 연산에 수행할 피연산자 빼서 연산한 뒤 다시 스택에 넣어라
        else:
            stack.pop()
            output.append(int(output.pop()) + int(output.pop()))
    
    # 최종 연산 결과 반환
    return output.pop()

for t in range(10):
    N = int(input())
    input1 = list(input())
    # 출력합니다.
    print(f'#{t+1} {prefix_cal1(N, input1)}')
