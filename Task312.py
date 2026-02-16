class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def total_salary(self):
        return self.base_salary

class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent

    def total_salary(self):
        return self.base_salary * (1 + self.bonus_percent / 100)

class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects

    def total_salary(self):
        return self.base_salary + self.completed_projects * 500


class Intern(Employee):
    def total_salary(self):
        return self.base_salary


vvod = input().split()
role = vvod[0] 
name = vvod[1] 
salary = int(vvod[2]) 


if role == "Manager":
    bonus = int(vvod[3])
    obj = Manager(name, salary, bonus)
elif role == "Developer":
    projects = int(vvod[3])
    obj = Developer(name, salary, projects)
else:
    obj = Intern(name, salary)

print(f"Name: {obj.name}, Total: {obj.total_salary():.2f}")
