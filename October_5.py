#October 5
'''
l1= [10,20,30,40,50]
#Printing the list using for loop
for i in l1:
    print(i, end=',')

#Printing the list using while loop
index = 0
while index < len(l1):
    print(l1[index], end = ',')
    index += 1

#Printing numbers from 100 to 200
i=100
while i>=100 and i<=200:
    print (i,end=',')
    i+=1
s1 = 'Computer'
for i in s1:
    print (i)
# User will enter a statement find out how many words are there in a statement
s1=input("Enter a statement : ")
a=1
for i in s1:
    if i==" ":
        a+=1
print('There are', a ,"# using for loop")
# using split funciton
print("There are", len(s1.split()),"# using split function")

# Jump statements : break and continue
for i in range (11):
    if i == 5 :
        break
    print(i, end=",")
for i in range(11):
    if i ==5:
        continue
    print(i, end=",")
# To print all odd numbers between 1 to 100
for i in range(1,101):
    if i%2==0:
        continue
    print(i, end =",")
#Program to check whether a number is prime number or not
n=int(input("Enter the number : "))
flag = True
for i in range (2,n):
    if n%i==0:
        flag = False
        print("Not a prime number")
        break
if flag == True:
    print("Prime no.")
# pass block
word = "python"
for alpha in word :
    if alpha=="h":
        pass
        print("this is pass block")
    print("Current word : ", alpha)
print("Good Bye")

# To print all the numbres between 1 and 100
for i in range(1,101):
    if i%2==0:
        pass
    else :
        print(i, end = ",")
# nested loops
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print (" ")

for i in range(1,6):
    for j in range (5,i,-1):
        print(" ", end=" ")
    for k in range(1,i+1):
        print ("*", end =" ")
    print("")
'''
#String
a='''Hello Students !
Welcome to the String Session !!'''
print(a)
'''
 #Forward and backward indexing
       H   E   L   L   O
Frwd   0   1   2   3   4
Bckd  -5  -4  -3  -2  -1

Syntax for slicing
[starting index : end index : step]
start = 0
end = -1
step = 1
'''
s1= 'COMPUTER'
print (s1[1:3])
print (s1[-1:-5:-1])
print (s1[1:-1:2])

