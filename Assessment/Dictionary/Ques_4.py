# Ques_4
# Write a Python program to match key and values both, in two dictionaries.
def match_key_values(dict1, dict2):
    matches = {key: dict1[key] for key in dict1 if key in dict2 and dict1[key] == dict2[key]}
    return matches
dict1 = eval(input("Enter first dictionary: "))
dict2 = eval(input("Enter second dictionary: "))
print("Matching key-value pairs:", match_key_values(dict1, dict2))