t = int(input())
case_1= input().split()
case_2= input().split()
case_3= input().split()

a = list()
b = list()
c = list()
d = list()

for i in range(len(case_1)):
    a.append(int(case_1[i]))
    a1 = max(a)
for i in range(len(case_2)):
    b.append(int(case_2[i]))
    b1 = max(b)
for i in range(len(case_3)):
    c.append(int(case_3[i]))
    c1 = max(c)

d.append(a1)
d.append(b1)
d.append(c1)

for i in range(1, t+1):
    print("#{}".format(i), d[i-1])


