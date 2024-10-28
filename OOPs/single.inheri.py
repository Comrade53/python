class parent:
    def func1(self):
        print("This is a function int the parent class")

class child(parent):
    def func2(self):
        print("This is function in the child class")

object=child()
object.func1()
object.func2()