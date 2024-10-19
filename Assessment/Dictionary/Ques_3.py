# Ques_4
# Write a Python program to create a dictionary from a string. ( Track the count of the letters from the string.)
def count_letters(input_string):
    letter_count = {}
    for letter in input_string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count
input_string = input("Enter a string: ")
print("Letter count dictionary:", count_letters(input_string))