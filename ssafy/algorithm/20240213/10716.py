def forth_cal(code):
    """
    params code: 후위 계산식
    return: 계산 결과
    """
    # 괄호나 다른 연산자가 존재하는 것인가?
    stack = []
    for oper in code:

        # 더하기
        if oper == '+':
            # 원소 뽑을 때 인덱스 에러 털기
            try:
                stack.append(stack.pop() + stack.pop())
            except IndexError:
                return 'error'

        # 빼기
        elif oper == '-':
            # 원소 뽑을 때 인덱스 에러 털기
            try:
                stack.append(stack.pop(-2) - stack.pop())
            except IndexError:
                return 'error'

        # 곱하기
        elif oper == '*':
            # 원소 뽑을 때 인덱스 에러 털기
            try:
                stack.append(stack.pop() * stack.pop())
            except IndexError:
                return 'error'

        # 나누기
        elif oper == '/':
            # 원소 뽑을 때 인덱스 에러 털기
            try:
                stack.append(stack.pop(-2) // stack.pop())
            except IndexError:
                return 'error'
        
        # 종료(반환할 때, 임시 스택에 결과 말고는 존재하지 않아야 한다.)
        elif oper == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'
        
        # 피연산자
        else:
            # 계산 시 타입 에러 방지
            stack.append(int(oper))

    # .이 나오지 않는 경우가 있을 수 있다.
    return 'error'

T = int(input())
for t in range(T):
    input_data = input().split()
    # 출력합니다.
    print(f'#{t+1} {forth_cal(input_data)}')