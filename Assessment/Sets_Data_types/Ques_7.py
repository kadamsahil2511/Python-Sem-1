# Ques_7
# Write a Python function to check if a list is a palindrome or not. Return true otherwise false.
def is_palindrome(input_list):
    return input_list == input_list[::-1]
input_str = input("Enter the list elements separated by space : ")
input_list = input_str.split()
print(is_palindrome(input_list))