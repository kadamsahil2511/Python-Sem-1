# Ques 2 Find length of a string in python without using len function

s2 = input('Enter the string : ')
l = sum(1 for i in s2)
print("Length of", s2, "is:", l)
