class Gfather:
    def __init__(self, Gfathername):
        self.Gfathername = Gfathername

class father(Gfather):
    def __init__(self, fathername, Gfathername):
        super().__init__(Gfathername)  # Call the constructor of Gfather
        self.fathername = fathername

class son(father):
    def __init__(self, sonname, fathername, Gfathername):
        super().__init__(fathername, Gfathername)  # Call the constructor of father
        self.sonname = sonname

    def print_name(self):
        print("Grandfather name:", self.Gfathername)  
        print("Father name:", self.fathername)
        print("Son name:", self.sonname)    

s1 = son('ram', 'sham', 'raju')
print(s1.Gfathername)
s1.print_name()
