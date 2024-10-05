'''
#Print multiplication table of a given number
n=int(input("Enter the number you want tabke for : "))
for i in range (1,11):
    print(n, "x", i,"=", i*n)
'''

#Count the total number of digits in a number
n=input("Entere a number : ")
a=0
for i in range(1,int(n)+1):
    a+=1
print("The digits in given number is", a)
    