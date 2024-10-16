# Ques_3
# Write a Python program to print the numbers of a specified list after removing even numbers from it.
def remove_even_numbers(input_list):
    return [num for num in input_list if int(num) % 2 != 0]
input_str = input("Enter the list elements separated by space : ")
input_list = input_str.split()
print(remove_even_numbers(input_list))