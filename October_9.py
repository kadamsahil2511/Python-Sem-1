#October 9
# Python functions
'''
With functions we don't need to write the same code again and again, we just have to call it when needed
'def()' is used to define a function
Syntax for functions
def function_name(parameters):
    "Function_docstring"
    function_suite
    return[expression]
#eg 
def message():
    print("Hello")
message()          #Calling the function
print(message())
#eg 2
def message(name, period):
    print('Hello', name)
    print ("Good", period)
message("Sahil", 'Morning')
message(period='Night', name = "Avey")
#eg3
def message(name, period='Morning'):
    print('Hello', name)
    print ("Good", period)
message("Sahil")
message(period='Night', name = "Avey")
#eg4
def sum(*numbers):
    s=0
    for n in numbers:
        s=s+n
    print('Sum of', numbers, '=', s)
sum(1,2,3,4,5,6,7,8,9,10)
#eg5
def sum(a,b):
    return a+b
print("Sum of 5 and 6 is", sum(5,6))

#Write a program accept numbers from user until user wants and then sum and average
def calc(num):
    s=0
    avg=0
    for i in num:
        s=s+i
        avg=s/len(num)
        return s, avg
num=[]
flag =False
while flag is False :
    a=input("Enter numbers to find sum and avg, enter again to exit : ")
    if a=="":
        flag=True
    else :
        num.append(int(a))
calc(num)
print("Sum of the numbersa is",s,"Average of numbers is",avg)
'''
# Calculator usinsg functions
def calc(a,b):
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mult(a,b):
        return a*b
    def div(a,b):
        return a/b
    return add(a,b), sub(a,b), mult(a,b), div(a,b)
print(calc(10,20))

