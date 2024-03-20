# def easy_palindrome_check(string):
#     """
#     :param string: 회문 검사를 수행해야 하는 문자열
#     :return: 회문 유무, (有:1, 無:0)
#     """

#     for i in range(len(string)//2):
#         if string[i] != string[-1-i]:
#             return 0
#     return 1

# import collections
# def easy_palindrome_check(Deque):
#     """
#     :param string: 회문 검사를 수행해야 하는 문자열
#     :return: 회문 유무, (有:1, 無:0)
#     """
    
#     while len(Deque) > 1:
#         if Deque.popleft() != Deque.pop():
#             return 0
#     return 1

def easy_palindrome_check(string):
    """
    :param string: 회문 검사를 수행해야 하는 문자열
    :return: 회문 유무, (有:1, 無:0)
    """
    if string != string[::-1]:
        return 0
    return 1

T = int(input())
for t in range(T):
    input_str = input()
    print(f'#{t+1} {easy_palindrome_check(input_str)}')
