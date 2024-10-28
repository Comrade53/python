 
class Department:
    department_name = "CSE"

    def show_department(self):
        print(self.department_name)

class ClassA:
    class_name = "A"

    def show_class(self):
        print(self.class_name)

class Student(Department, ClassA):
    def engg(self):
        print("Class name is:", self.class_name)
        print("Department name is:", self.department_name)

# Create an instance of Student
s1 = Student()
s1.show_class()          
s1.show_department()     
s1.engg() 
               


