# Ques_1
# Write a Python program to remove duplicates from the dictionary. 
def remove_duplicates(input_dict):
    result = {}
    seen_values = set()
    for key, value in input_dict.items():
        if value not in seen_values:
            result[key] = value
            seen_values.add(value)
    return result
input_dict = eval(input("Enter a dictionary: "))
print("Dictionary after removing duplicates:", remove_duplicates(input_dict))