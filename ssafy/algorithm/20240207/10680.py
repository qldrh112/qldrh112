    # def parentheses_check(lst):
    #     """
    #     params lst: 괄호 검사를 수행할 문자열
    #     return: 검사 결과 (짝이 맞음: 1, 맞지 않음: 0)
    #     """
    #     stack = []

    #     for i in range(len(lst)):

    #         # 여는 괄호 만나면 추가
    #         if lst[i] in ['(', '{']:
    #             stack.append(lst[i])

    #         # 소괄호 만났을 때
    #         elif lst[i] == ')':
    #             if len(stack) > 0 and stack[-1] == '(':
    #                 stack.pop(-1)
    #             else:
    #                 return 0

    #         # 중괄호 만났을 때
    #         elif lst[i] == '}':
    #             if len(stack) > 0 and stack[-1] == '{':
    #                 stack.pop(-1)
    #             else:
    #                 return 0

    #     if len(stack) == 0:
    #         return 1
    #     else:
    #         return 0

    def parentheses_check(string):
        """
        params string: 괄호 검사를 수행할 문자열
        return: 검사 결과 (짝이 맞음: 1, 맞지 않음: 0)
        """
        stack = []
        table = {
        '}': '{',
        ')': '(',
        }

        for i in range(len(string)):
            if 39 >= ord(string[i]) or 42 <= ord(string[i]) <= 122:
                continue
            # { 또는 (이 입력
            elif string[i] =='{' or string[i] == '(':
                stack.append(string[i])
            # 스택이 비었거나({이나 (이 들어오지 않은 채로 )과 }이 들어옴), 괄호의 쌍이 맞지 않은 경우
            else:
                try:
                    if not stack or table[string[i]] != stack.pop():
                        return 0
                except IndexError:
                    return 0
            
        if len(stack):
            return 0
        else:
            return 1


    T = int(input())
    for t in range(T):
        input_data = input()
        print(f'#{t+1} {parentheses_check(input_data)}')
