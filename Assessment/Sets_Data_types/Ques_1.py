# Ques_1
# Write a Python program to remove duplicates from a list.
def remove_duplicates(input_list):
    return list(set(input_list))
input_str = input("Enter the list elements separated by space : ")
input_list = input_str.split()
print(remove_duplicates(input_list))