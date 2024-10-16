# Ques_4
# Write a Python program to find the second smallest number in a list.
def second_smallest(input_list):
    unique_list = list(set(input_list))
    unique_list.sort()
    return unique_list[1] if len(unique_list) > 1 else None
input_str = input("Enter the list elements separated by space : ")
input_list = input_str.split()
print(second_smallest(input_list))