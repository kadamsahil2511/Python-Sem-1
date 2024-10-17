# Ques_11
# program to count number of vowels using sets in given string
def count_vowels(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return len([char for char in input_string if char in vowels])
input_string = input("Enter a string: ")
print("Number of vowels in the given string:", count_vowels(input_string))