# #October 4
# #Loop Control in Python
# '''
# There are only 2 types of loop statmentes
# 1. while
# 2. for
# '''
# # while loop syntax
# # while (condition) :
# #     code execution if the ceondition is true
# # code executes if the condition is false
# # eg
# # Print numbers from 1 to 10 

# a=1 # counte initialisation          Step 1
# while a<=10 : # condition            Step 2
#     print(a, end=" ") # loop body    Step 3
#     a+=1 # increment                 Step 4
# print("End of the loop")

# # Print numbers from 10 to 1 

# a=10 # counte initialisation         Step 1
# while a>=1 : # condition             Step 2
#     print(a, end=" ") # loop body    Step 3
#     a-=1 # increment                 Step 4
# print("End of the loop")

# #For loop syntax
# # for iterating_Var in sequences :
# #     statement

# # eg. Print numbers from 1 to 10
# for i in range(1,11):
#     print(i, end = ' ')
# print("End of the loop")

# #Print natural numbers till user has specified
# a=int(input("Upto what number natural number should be printed : "))
# for i in range(1,a+1):
#     print(i, end = " ")
# print("")

#if you include 3rd parameter in range it is step value, if u don't mention then default value is 1
#if you only include 1 paremeter in range it is considered as stop value and start value be default is 0

#Calculate the sum of the elements of give list
l1=[1,2,3,5,6,7,8,9,10]
a=0
for i in l1:
   a=a+i 
print("Sum of all the elements in the list is",a)

#Calculate the factorial also show the calcualtions
n=input("Enter the number to calculate factorial : ")
for i in range(1,int(n)+1):
   print(i, end = "*")
   a=a*i
print("The factorial of",n,"is", a)