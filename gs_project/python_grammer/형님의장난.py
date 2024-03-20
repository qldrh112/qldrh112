import random

a = '으'
b = '응'
c = 'ㅇ'
d = 'ㅡ'

a2 = []

for i in range(100):
    a1 = []
    for j in range(73):
        a1.append(random.choice([a, b, b, b, b, b, b, b, b, c, d]))
        a2.append(random.choice([a, b, b, b, b, b, b, b, b, c, d]))
    print(a1, sep='')

print(f"ㅇ: {round(a2.count('ㅇ')/len(a2), 3)*100}%\nㅡ :{round(a2.count('ㅡ')/len(a2), 3)*100}%\n으: {round(a2.count('으')/len(a2), 3)*100}%\n응: {round(a2.count('응')/len(a2), 3)*100}%")
