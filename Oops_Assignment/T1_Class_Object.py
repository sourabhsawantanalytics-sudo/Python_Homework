class Student:                                  #class
    def __init__(self,name, roll_no, course, email):   # constructor
        self.name    = name                     #current object attribute
        self.roll_no = roll_no
        self.course  = course
        self.email   = email
        

    def display_student(self):                  # method
        print(self.name, self.roll_no, self.course, self.email)

s1 = Student("Aman Joshi", 101, "Data Science", "aman@gmail.com") #object create
s2 = Student("Ram Kadam", 102, "Data Analyst", "ram@gmail.com")   #object create

s1.display_student()                            #call method
s2.display_student()                            #call method
