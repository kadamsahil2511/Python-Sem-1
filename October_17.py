# October_17
# Python program to show that the variables with a value assigned in class declaration, are class variables
'''
from sys import argv


class CSStudent:
    stream = 'IT' #Class Variable
    def __init__(self, name, roll):
        self.name =name #Instance Variable
        self.roll =roll #Instance Variable

# Objects of CSStudent class
a = CSStudent('ABC', 1)
b = CSStudent('DEF', 2)

print("Student 1")
print(a.stream)# prints "IT"
print(a.roll)# prints "1"
print(a.name)# prints "ABC"

print("Student 2")
print(b.stream)# prints "IT"
print(b.roll)# prints "2"
print(b.name)# prints "DEF"

# Variables can be accessed using class name also

print(CSStudent.stream) # prints "IT"

#Now if we change the stream for just 'a', it won't be changed for 'b'
a.stream = 'ETC'
print("a.stream",a.stream) #prints 'ETC' 
print("b.stream",b.stream) #prints 'IT'

#To change the stream for all instances of the class, we can change it directly from the class 
CSStudent.stream = 'CS'

#Different types of constructors in Python
#1. Default constructor
#2. Parameterized constructor

class const_types:
    def __init__(self):
        print("Default Constructor")
    def __init__(self,arg1=0):
        data = arg1
        print("Paramaterized Constructor")
    def __init__(self,other):
        self.data=other.data
        print("Parametrised Construction")
# obj1=const_types()
# obj2=const_types(10)
 
#Operations on attributes
getattr(obj,name, default): #It is used to access the attribute of the object.
setattr(obj, name, value):# It is used to set a particular value to the specific attribute of an object.
delattr(obj, name): #It is used to delete a specific attribute.
hasattr(obj, name):# It returns true if the object contains some specific attribute.
 '''
class student:
    #Attributes (data)
    def __init__(self):
        self.roll=0
        self.sname=''

    #Methods
    # def setdata(self):
    #     self.roll=int(input("Enter your roll no : ")) 
    #     self.sname=input("Enter your name: ")
    def getdata(self):
        print("Roll No: ",self.roll) 
        print("Name : ",self.sname)

s1=student()#object created
# s1.setdata()
 
# print(getattr(s1, 'sname'))
# print(hasattr(s1, 'roll'))
# setattr(s1, 'sname', 'Vijay')
# print(getattr(s1, 'sname'))
# print(hasattr(s1, 'sname'))
# s1.getdata()
# delattr(s1, 'sname')

print(student.__doc__)
print(student.__dict__)
print(student.__name__)
print(student.__module__)

#Destructor