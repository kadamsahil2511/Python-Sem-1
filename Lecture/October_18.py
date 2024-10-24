# October_18
#Inheritance
'''
syntax 
classs derived-class(base-class)
    <class-suite>
class derive-class(<base class 1>,<base class 2>,<base class 3>.........<base class n>)
    <class-suite>

class vehicle:
    def __init__(self):
        self.make=''
        self.model=''
    def DisplayDetails(self):
        print("Make : ",self.make,"\nModel : ",self.model)
class swift(vehicle):
    def __init__(self):
        self.make='Hyundai'
        self.model='V2'
o2=swift()
o2.DisplayDetails()

class vehicle:
    def __init__(self,mk,md):
        self.make=mk
        self.model=md
        self.speed=50
    def DisplayDetails(self):
        print("Make : ",self.make,"\nModel : ",self.model)
class swift(vehicle):
    def __init__(self,a,b):
        super().__init__(a,b)
        self.speed=100
    def speed_details(self):
        print("speed : ",self.speed)
o2=swift("Hyundai", "Dzire")
o2.DisplayDetails()
o2.speed_details()

# Hierarchical
'''
class student:
    def setPersonal(self):
        self.roll=input("Enter the roll no : ")
        self.name=input("Enter the name: ")
    def getPersonal(self):
        print("Roll:", self.roll, "\nName:", self.name,end="\t")

class fy(student):
    def getmarks (self):
        self.s1=int(input("Enter subject marks: "))
        self.s2=int(input("Enter subject marks: "))
        self.s3=int(input("Enter subject marks: "))
    def showmarks(self):
        self.total=(self.s1 + self.s2 + self.s3)
        print("Total:", self.total)
class sy(student):
    def getmarks(self):
        self.s1=int(input("Enter subject marks: "))
        self.s2=int(input("Enter subject marks: "))
        self.s3=int(input("Enter subject marks: "))
        print("Total: ", self.total)
        self.s4=int(input("Enter subject marks: "))

    def showmarks(self):
        self.total=(self.s1+self.s2+self.s3+self.s4)
fy_std1=fy() #First year students
sy_std1=sy() #Second year students
'''
print("First year Student")
fy_std1.setPersonal()
fy_std1.getmarks()

print("Second year Student")
sy_std1.setPersonal()
sy_std1.getmarks()

print("Students Details")

fy_std1.getPersonal()
fy_std1.showmarks()
sy_std1.getPersonal()
sy_std1.showmarks()
'''
# Ques - for bank custmer create base class for saving and loan account and create a multiple inheritance

'''
Syntax for multilevel inheritance

Syntax for multiple inheritance
class Base1:
    <class-suite>

class Base 2:
    <class-suite>

class BaseN:
    <class-suite>

class Derived(Base1, Base2, BaseN):
    <class-suite>

print(issubclass(fy,student))
print(issubclass(student,fy))
print(isinstance(fy_std1,fy))
print(isinstance(fy_std1,sy))
print(isinstance(fy_std1,student))
'''

#Method Overriding
#Example 
class Animal :
    def speak(self):
        print("Speaking")
class Dog(Animal):
    def speak(self):
            print("Barking")
d=Dog()
d.speak()

class Distance:
    def __init__(self,n): 
        self.n=n

    def __add__(self,d2): 
        result=self.n+d2.n
        return result

    def __sub__(self,d2): 
        result=self.n-d2.n
        return result

    def __lt__(self,d2):
        result=self.n<d2.n
        return result

d1=Distance(10)
d2=Distance(45)
print(d1+d2)
print(d1-d2)
print(d1<d2)

#build a class complex having attributes real and imaginary. and perform complex number addition and subtraction operation
