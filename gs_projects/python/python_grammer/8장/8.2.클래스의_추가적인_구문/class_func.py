#클래스를 선언합니다.
class Student:
    # 클래스 변수
    count = 0
    students = []

    # 클래스 함수
    @classmethod
    def print(cls):
        print("------학생 목록------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------ ------ ------")

    # 인스턴스 함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math +\
        self.english + self.science
    
    def get_average(self):
        return self.get_sum()/4
    
    def __str__(self):
        return "{}\t{}\t{}".format(\
            self.name,
            self.get_sum(),
            self.get_average())

# 학생 리스트를 선언합니다.
Student("이규석", 98, 98, 88, 95)
Student("정선기", 92, 98, 96, 98)
Student("박태수", 76, 96, 94, 90)
Student("장시형", 98, 92, 96, 92)
Student("장지호", 95, 98, 98, 98)
Student("김홍성", 64, 88, 92, 92)
Student("심대훈", 82, 86, 98, 88)
Student("나도경", 88, 74, 78, 92)
Student("박현희", 97, 92, 88, 95)
Student("신우형", 45, 52, 72, 78)

# 현재 생성된 학생을 모두 출력합니다.
Student.print()