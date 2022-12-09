"""class Student:
    def __init__(self,name,branch,reg,c1,c2,c3,c4,c5,m1,m2,m3,m4,m5):
        self.name = name
        self.branch = branch
        self.reg = reg
        self.course1 = c1
        self.course2 = c2
        self.course3 = c3
        self.course4 = c4
        self.course5 = c5
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3
        self.marks4 = m4
        self.marks5 = m5
    def display(self):
        self.total = (self.marks1+self.marks2+self.marks3+self.marks4+self.marks5)
        self.per = (self.total/500)*100
        print("Student Name :",self.name)
        print("Student Branch :",self.branch)
        print("Student Reg. No :",self.reg)
        print("Course Name :",self.course1)
        print("Course Name :",self.course2)
        print("Course Name :",self.course3)
        print("Course Name :",self.course4)
        print("Course Name :",self.course5)
        print("Marks :",self.marks1)
        print("Marks :",self.marks2)
        print("Marks :",self.marks3)
        print("Marks :",self.marks4)
        print("Marks :",self.marks5)
        print("Percentage :",self.per)
a = Student("abc","cse",123,"phy","html","Physics","mec","maths",90,93,94,95,96)
a.display()
"""

class Volume:
    def __init__(self,r,h):
        self.radius = r
        self.height = h
        self.sphere = (1.33)*3.14*(self.radius**3)
        self.cone = (0.33)*3.14*(self.radius*self.radius*self.height)
        self.cyl = 3.14*(self.radius*self.radius*self.height)
    def display(self):
        print("Volume of Sphere :",self.sphere)
        print("Volume of Cone :",self.cone)
        print("Volume of Cylinder :",self.cyl)
a = Volume(10,15)
a.display()
print()
b = Volume(3.8,4.9)
b.display()
