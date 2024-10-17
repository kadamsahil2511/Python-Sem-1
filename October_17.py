# October_17
# Python program to show that the variables with a value assigned in class declaration, are class variables

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

