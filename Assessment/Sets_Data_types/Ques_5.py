# Ques_5
# Write a Python program to split a list every Nth element.
def split_list(input_list, n):
    return [input_list[i:i + n] for i in range(0, len(input_list), n)]
input_str = input("Enter the list elements separated by space : ")
input_list = input_str.split()
n = int(input("Enter the Nth element : "))
print(split_list(input_list, n))