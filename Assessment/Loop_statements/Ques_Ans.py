'''
#Print multiplication table of a given number
n=int(input("Enter the number you want tabke for : "))
for i in range (1,11):
    print(n, "x", i,"=", i*n)
'''

#Count the total number of digits in a number **not finished
# n=input("Enter a number : ")
# a=
# while a!=0:
#     a=a+1
#     continue
# print("The total number of digits in given number is", a)

#Print reverse order using a loop
l1=(input("Enter elements of the list : ")).split()
for i in range(len(l1),0,-1):
    print(i, end=" ")
