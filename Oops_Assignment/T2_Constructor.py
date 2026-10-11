class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_details(self):
        print(self.employee_id, self.name, self.department, self.salary)

e1 = Employee("E101", "Abhay More", "IT", 35000)
e2 = Employee("E102", "Ram Jadhav", "HR", 28500)
e3 = Employee("E103", "Priya Kadam", "Admin", 29400)

# e1.display_details()
# e2.display_details()
# e3.display_details()

employees = [e1,e2,e3]
for i in employees:
    print(i)
    i.display_details()