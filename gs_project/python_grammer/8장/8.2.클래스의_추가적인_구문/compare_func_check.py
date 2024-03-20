# 클래스를 선언합니다.
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +\
    self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average())

    def __eq__(self, value):
        return self.get_average() == 90
    def __ne__(self, value):
        return self.get_average() != 90
    def __gt__(self, value):
        return self.get_average() > 90
    def __ge__(self, value):
        return self.get_average() >= 90
    def __lt__(self, value):
        return self.get_average() < 90
    def __le__(self, value):
        return self.get_average() <= 90
    
# 학생 리스트를 선언합니다.
students = [
    Student("이규석", 87, 98, 88, 95),
    Student("정선기", 92, 98, 96, 98),
    Student("박태수", 76, 96, 94, 90),
    Student("장시형", 98, 92, 96, 92),
    Student("장지호", 95, 98, 92, 92),
    Student("김홍성", 64, 88, 92, 92)
]

# 학생을 선언합니다.
test = Student("A", 90, 90, 90, 90)


# 출력합니다.
print("test == 90:", test == 90)
print("test != 90:", test != 90)
print("test > 90:", test > 90)
print("test >= 90:", test >= 90)
print("test < 90:", test < 90)
print("test <= 90:", test <= 90)