class Employee:
    def __init__(self,employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def display_info(self):
        print("ID:", self.employee_id)
        print("Name:", self.name)
        print("Salary:", self.salary)

    def annual_salary(self):
        return self.salary * 12


class Developer(Employee):
    def __init__(self, employee_id, name, salary, p_language):
        super().__init__(employee_id, name, salary)
        self.p_language = p_language

    def display_info(self):
        super().display_info()
        print("Role: Developer")
        print("P language:", self.p_language)

class Tester(Employee):
    def __init__(self, employee_id, name, salary, testing_tool):
        super().__init__(employee_id, name, salary)
        self.testing_tool = testing_tool

    def display_info(self):
        super().display_info()
        print("Role: Tester")
        print("Testin Tool:",self.testing_tool)


class Manager(Employee):
    def __init__(self, employee_id, name, salary, team_size):
        super().__init__(employee_id, name, salary)
        self.team_size = team_size

    def display_info(self):
        super().display_info()
        print("Role: Manager")
        print("Team Size:", self.team_size)

# Objects
employees = [
    Developer(101, "Neha",75000, "Python"),
    Developer(102, "Rahul",81000, "Java"),
    Tester(103, "Ram", 60000, "Selenium"),
    Tester(104, "Pratik", 58000, "Postman"),
    Manager(105, "Sagar", 100000, 8) 
]

# Iterate and display
for emp in employees:
    emp.display_info()
    print("Annual Salary:", emp.annual_salary())
    print("-" * 70)
