# Ques_10
# Write a Python program to Convert Set to one String
def set_to_string(input_set):
    return ' '.join(map(str, input_set))
input_set = set(map(int, input("Enter elements of the set separated by space: ").split()))
print("Set converted to string:", set_to_string(input_set))