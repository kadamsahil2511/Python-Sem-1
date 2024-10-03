# October 3 
# the else if ladder
# syntax
if expresssion 1 :
    block of statement 
elif expresssion 1 :
    block of statement 
elif expresssion 1 :
    block of statement 
elif expresssion 1 :
    block of statement 
else :
    block of statement

#program to find out whether a student is pass or fail

per=float(input('Enter the percentage : '))

if (per>=90 and per<=100) :
    print('Merit')
elif (per>75 and per<90) :
    print('Distinction')
elif (per>=60 and per<75) :
    print('First class')
elif (per>=75 and per<45) :
    print('Second class')
elif (per>45 and per<35) :
    print('Third class')
elif (per>=35 and per<45) :
    print('Pass')
else :
    print('Fail')

#User will enter month number and print no of days
a=int(input('Enter the month number : '))
if a>0 and a<=12 :
    if a in (1,3,5,7,8,10,12):
        print('The month has 31 days')
    elif a in (4,6,9,11):
        print('The months has 30 days')
    else :
        print("The month has 28 days and 29 if it's a leap year")
else :
    print("The months you've entered is invalid")