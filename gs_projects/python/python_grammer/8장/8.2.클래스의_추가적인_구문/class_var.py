# 클래스를 선언합니다.
class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        # 인스턴트 변수 초기화
        self.name = name
        self.name = korean
        self.name = math
        self.name = english
        self.name = science

        # 클래스 변수 설정
        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

# 학생 리스트를 선언합니다.
student = [
    Student("이규석", 87, 98, 88, 95),
    Student("정선기", 92, 98, 96, 98),
    Student("박태수", 76, 96, 94, 90),
    Student("장시형", 98, 92, 96, 92),
    Student("장지호", 95 ,98, 98, 98),
    Student("김홍성", 64, 88, 92, 92)
]

# 출력합니다.
print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))