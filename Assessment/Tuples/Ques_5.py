# Ques_5
# Write a Python program to convert a given string to a tuple
def string_to_tuple(string):
    return tuple(map(str,string.split(',')))

string = input("Enter comma-separated values: ")
result = string_to_tuple(string)
print("Tuple:")
print(result)