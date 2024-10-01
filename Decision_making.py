a=50
b=100
#sytax for If condition
if a<b:
    #code executes if the condition is true for eg.
    print('a is less than b')
else :
    print('b is less than a')

#eg 2
colour = input('Enter your favourite colour : ').lower()
if colour == "red" : 
    print('Red Zone')
else :
    #code executes if the condition is false
    print('End of program')

#eg 3
marks = int(input('Enter student marks'))
if marks>=35 : print('PASS')
else : print('FAIL')

#eg 4
n=int(input('Enter a number to check : '))
if n%2==0 :
    print("The number is even")
else :
    print("The number is odd")

#progam to demonstrate ternary operator 
a=10
b=15
print("Both are equal" if a ==b else "a is greater" if a>b else 'b is minimmum')

# eg 2
a=int(input('Enter the number to be checked'))
print('The number is even' if a%2==0 else 'The number is odd')

#Nested control statements 
a,b,c=5,6,7
if(a>b):
    if (a>c):
        print('a is greater')
    else :
        print ('c is greater')
else :
    if (b>c):
        print('b is greater')
    else :
        print('c is greater')