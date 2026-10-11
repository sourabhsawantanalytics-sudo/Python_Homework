class Employee:    # class
    def __init__(self, name, salary):   #constructor
        self.name = name       # current obj attribute
        self.salary = salary   # current obj attribute

    def display_info(self):     # employee method def
        print("Name:", self.name)
        print("Salary:", self.salary)

class Developer(Employee):   # class developer inherit class employee
    def __init__(self, name, salary, p_lang):  # method2
        super().__init__(name, salary) # class employee (parent) ke constructor ko call karta hai
        self.p_lang = p_lang

    def show_developer_info(self): # method3
        self.display_info()  # employee method call
        print("Programming Language:", self.p_lang)



dev = Developer("Neha", 75000, "Python" ) # object1
dev1 = Developer("Pratik", 91000, "Java") # object 2

dev.show_developer_info() # method call
print("*" * 80)
dev1.show_developer_info()

