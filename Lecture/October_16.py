# October_16
# Q - For different types of operations which data type is faster with explanation
'''
Syntax for classes in python
class ClassName:
    #statement_suite
class simplestL
    pass
s=simplest() #create an instance
'''
'''
class student :
    #Attributes
    roll=0
    std_name=""
    marks=0

    def setdata(self):
        self.roll=int(input("Enter your roll no : "))
        self.std_name=input("Enter your name : ")
        self.marks=int(input("Eneter your marks : "))
    def getdata(self):
        print("Roll Number : ", self.roll)
        print("Student Name : ", self.std_name)
        print("Student marks :", self.marks)
        if self.marks>35:
            print("Result = Pass")
        else :
            print("Result = Fail")
s1=student() #created an object
# s2=student() 
s1.setdata()
# s2.setdata()
print("-"*20)
print("Student Details")
print("-"*20)
s1.getdata()
# s2.getdata()
'''
#constructor & destructor
'''
Syntax::
A constructor always has a name init and the name init is prefixed and suffixed with a double underscore(__). We declare a constructor using def keyword,
just like methods.

def__init__(self):
    #body of the constructor
'''
class sample:
    def __init__(self):
        self.n=10
    def display(self):
        print("Number", self.n)
    def __del__(self):
        print("Object destroyed")
obj1=sample()  # Constructor being called automatically
obj1.display()