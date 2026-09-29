class Student:
    def __init__(self, roll, name, marks, address):
        self.roll_no = roll
        self.name = name
        self.marks = marks
        self.address = address


class Teacher:
    def __init__(self, name, salary, dep, addr):
        self.name = name
        self.salary = salary
        self.dep = dep
        self.address = addr


class College:
    def __init__(self, name, students, teachers):
        self.name = name
        self.students = students
        self.teachers = teachers


s = Student(1, "Aman", 78, "Pune")
t = Teacher("Sagar", 41000, "Computer", "Nashik")

c = College("Desai College", s, t)

print(c.name)
print(c)
print(type(c))
print(id(c))
