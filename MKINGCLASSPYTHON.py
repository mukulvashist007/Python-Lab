print("""HIMANSHU SINHA
ROLL NO -2K18CSUN01064
CLASS -B-TECH CSE 4A""")
class Triangle:
    a=0
    b=0
    c=0
    def create_triangle(self):
        self.a=int(input("Enter The First Side"))
        self.b=int(input("Enter The Second Side "))
        self.c = int(input("Enter The Third Side "))
    def printside(self):
        print(self.a)
        print(self.b)
        print(self.c)

tr=Triangle()
tr.create_triangle()
print("The Sides Of Triangle are")
tr.printside()

class halwa:
    a=""
    def gets(self):
        self.a=input("Enter The String")
        return (self.a)
ha=halwa()
print("THE INPUT STRING IS" ,ha.gets())

class Rectangle:
    w=0.0
    l=0.0
    def calper(self):
        self.l=int(input("Enter The Length"))
        self.w=int(input("Enter The width"))
        return (2*(self.l+self.w))
r1=Rectangle()
print("The Perimeter of Rectangle is",r1.calper())

class Circle:
    rad=0.0
    def __init__(self):
        self.rad=float(input("Enter The Radius"))
    def areac(self):
        return (3.14*self.rad*self.rad)
    def perr(self):
        return (2*3.14*self.rad)
c1=Circle()
print("The Area Of circle is" ,c1.areac())
print("The Perimeter of rect is" , c1.perr())

class Circle2:
    rad=0.0
    def __init__(self):
        self.rad=float(input("Enter The Radius"))
    def areac(self):
        return (3.14*self.rad*self.rad)
    def circum(self):
        return (2*3.14*self.rad)
c2=Circle2()
print("The Area Of circle is" ,c2.areac())
print("The Perimeter of rect is" , c2.perr())

class Temp:
    f=0.0
    c=0.0
    def convf(self):
        self.f=int(input("Enter the Temp in F"))
        return ((self.f-32)/1.8)
    def convc(self):
        self.c=int(input("Enter The Temp in c"))
        return ((self.c*1.8)+32)
te=Temp()
print("The Conversion of F to C is",te.convf())
print("The Conversion of C to F is", te.convc())

class student():
    name=""
    marks=0
    age=0
    Roll_No=""
    def display(self):
        return (self.name,self.marks,self.Roll_No)
    def setage(self):
        self.age=int(input("Enter The Age of Student"))
        return (self.age)
    def setmarks(self):
        self.marks=int(input("Enter The Marks Of Student"))
        return (self.marks)
stu=student()
stu.name="Halwa"
stu.marks=2000
stu.Roll_No="2K18CSUN01064"
print(stu.display())
print("The age of Student is", stu.setage())
print("The Update Marks Of Student is", stu.setmarks())

class Time:
    hour = 0
    hour1 = 0
    min = 0
    min1 = 0
    tothr=0
    totmin=0

    def addTime(self):
        self.hour = int(input("Enter The Hour "))
        self.min = int(input("Enter the minute"))
        self.hour1 = int(input("Enter Another hour"))
        self.min1 = int(input("Enter Another Minute"))

    def displaytime(self):
        self.tothr=self.hour + self.hour1
        self.totmin=self.min + self.min1
        print(self.tothr,"Hour and ",self.totmin,"min")
    def displaymin(self):
        return (60*self.tothr+self.totmin)




b1 = Time()
b1.addTime()
print("The Total Time is")
b1.displaytime()
print("The Total Minute is",b1.displaymin())

class reversestring:
    a=""
    def rev_fun(self):
        self.a=input("Enter The String ")
        return self.a[::-1]
rev=reversestring()
print(rev.rev_fun())

