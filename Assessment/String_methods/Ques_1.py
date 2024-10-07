# Ques_1 Python program to check whether the string is Symmetrical or Palindrome

s1=input("Enter the string : ").lower()
if s1 == s1[::-1]:
    print(s1, "is a palindrome")
else :
    print(s1,'is not a palindrome')
