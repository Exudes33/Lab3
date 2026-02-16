class Person:
    def __init__(self, name):
        self.name = name  


class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa    

    def display(self):
       
        print(f"Student: {self.name}, GPA: {self.gpa}")

a = input().split()
имя = a[0]
оценка = a[1]

student = Student(имя, оценка)
student.display()
