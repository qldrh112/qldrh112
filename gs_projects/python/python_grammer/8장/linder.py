class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.science = science
        self.english = english

    def get_sum(self):
        return self.korean + self.math +\
        self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())
    
    

if __name__ == "__main__":
    
    students = [
        Student("이규석", 87, 98, 88, 95),
        Student("정선기", 92, 98, 96, 98),
        Student("박태수", 76, 96, 94, 90),
        Student("장시형", 98, 92, 96, 92),
        Student("장지호", 95, 98, 98, 98),
        Student("김홍성", 64, 88, 92, 92)
    ]

    print("이름", "총점", "평균", sep="\t")
    
    for student in students:
        print(student.to_string())