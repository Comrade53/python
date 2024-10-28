class School:
    def func1(self):
        print("This is a function in the school")

class Student1(School):
    def func2(self):
        print("This is a function in student 1")

class Student2(School):
    def func3(self):
        print("This is a function in student 2")

class Student3(Student1):
    def func4(self):
        print("This is a function in student 3")

obj = Student3()

obj.func1()  
obj.func2()  
obj.func4()  
