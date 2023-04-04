from person import Person

class Student(Person):
    class_name = '公信班'
    def __init__(self,name,age,gender,
                 school,grade,score):
        super(Student, self).__init__(name,age,gender)
        self.school = school
        self.grade = grade
        self.score = score

    def average_score(self):
        pass

