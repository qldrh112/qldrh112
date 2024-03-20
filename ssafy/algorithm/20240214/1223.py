def postfix_cal(N, formula):
    """
    params N: 계산식의 길이(int)
    params formula: 중위 계산식(string)
    return: 계산 결과(int)
    operand_stack: 피연산자(list)
    operator_stack: 연산자(list)
    """
    operand_stack = []
    operator_stack = []

    for i in range(N):
        
        # 피연산자일 때
        if str.isdigit(formula[i]):
            operand_stack.append(int(formula[i]))

        # 연산자 스택에 아무 것도 없다면
        elif len(operator_stack) == 0:
            operator_stack.append(formula[i])

        # '*' 을(를) 받았을 때
        elif formula[i] == '*':
            # 연산자 스택의 맨 위가 '*' 일 때
            if operator_stack[-1] == '*':
                operand_stack.append(operand_stack.pop() * operand_stack.pop())
            else:
                operator_stack.append('*')

        # '+' 을(를) 받았을 때
        else:
            # 연산자 스택의 맨 위가 '*' 일 때
            if operator_stack[-1] == '*':
                operator_stack.pop()
                operand_stack.append(operand_stack.pop() * operand_stack.pop())
                operator_stack.append('+')
            else:
                operand_stack.append(operand_stack.pop() + operand_stack.pop())

    while len(operator_stack) > 0:
        if operator_stack.pop() == '*':
            operand_stack.append(operand_stack.pop() * operand_stack.pop())
        else:
            operand_stack.append(operand_stack.pop() + operand_stack.pop())

    return operand_stack.pop()

for t in range(10):
    N = int(input())
    input_str = input()
    # 출력합니다.
    print(f'#{t + 1} {postfix_cal(N, input_str)}')
