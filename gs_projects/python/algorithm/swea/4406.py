"""
메모리: 58,512 kb
실행시간: 148 ms
"""
# import re
#
#
# def delete_vowel(string):
#     return re.sub('[^aeiou]', '', string)

def delete_vowel(string):
    tmp = ''
    for i in range(len(string)):
        if not vowel.get(string[i]):
            tmp += string[i]

    return tmp


vowel = {
    'a': '1',
    'e': '1',
    'i': '1',
    'o': '1',
    'u': '1',
}
T = int(input())
for t in range(T):
    input_string = input()
    print(f'#{t+1} {delete_vowel(input_string)}')