# Ques_2
# Write a Python program to combine two dictionary by adding values for common keys.
def combine_dictionaries(dict1, dict2):
    combined_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}
    return combined_dict
dict1 = eval(input("Enter first dictionary: "))
dict2 = eval(input("Enter second dictionary: "))
print("Combined dictionary:", combine_dictionaries(dict1, dict2))